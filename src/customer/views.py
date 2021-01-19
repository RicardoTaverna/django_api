import json
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import ContactsVarejao, ContactsMacapa
from .serializers import ContactsMacapaSerializer, ContactsVarejaoSerializer


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def contacts_add(request):
    """Endpoint para adicionar cliente."""
    content = {
        'user': request.user,
        'auth': request.auth,
    }
    
    if str(content['user']).lower() == 'macapa':
        print(request.data['contacts'])
        serializer = []
        for contact in request.data['contacts']:
            print(contact)
            contact['cellphone'] = _format_phone(contact['cellphone'])
            serializer_item = ContactsMacapaSerializer(data=contact)
            if not serializer_item.is_valid():
                return Response(serializer_item.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer_item.save()
            serializer.append(serializer_item.data)
        print(serializer)
        return Response(json.dumps(serializer), status=status.HTTP_201_CREATED)
        
        
    
    if str(content['user']).lower() == 'varejao':
        serializer = ContactsMacapaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(using='postgres')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response("400, Possivel erro no nome do usuario.", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def contacts_macapa(request):
    customer = ContactsMacapa.objects.all()
    serializer = ContactsMacapaSerializer(customer, many=True)
    return Response(serializer.data)


def _format_phone(phone: str) -> str:
    """Função para formatar o telefone +xx (xx) xxxxx-xxxx.

    Args:
        phone (str): telefone sem formatação

    Returns:
        str: telefone formatado
    """
    formated_phone = "+" + phone[0:2] + " (" + phone[2:4] + ") " + phone[4:9] + "-" + phone[9:13]
    return formated_phone
