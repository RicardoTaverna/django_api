import json
from datetime import datetime
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
            contact['cellphone'] = _format_phone(contact['cellphone'])
            serializer_item = ContactsMacapaSerializer(data=contact)
            if not serializer_item.is_valid():
                return Response(serializer_item.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer_item.save()
            serializer.append(serializer_item.data)
        return Response(json.dumps(serializer), status=status.HTTP_201_CREATED)

    if str(content['user']).lower() == 'varejao':
        selectedObject = ContactsVarejao()
        serializer = []
        for contact in request.data['contacts']:
            serializer_item = ContactsVarejaoSerializer(data=contact, instance=selectedObject)
            if not serializer_item.is_valid():
                return Response(serializer_item.errors, status=status.HTTP_400_BAD_REQUEST)
            selectedObject = serializer_item.create(serializer_item.validated_data)
            selectedObject.save(using='postgres')
            serializer.append(serializer_item.data)
        return Response(json.dumps(serializer), status=status.HTTP_201_CREATED)
            
    return Response("404, Erro no nome do usuario.", status=status.HTTP_404_NOT_FOUND)


def _format_phone(phone: str) -> str:
    """Função para formatar o telefone +xx (xx) xxxxx-xxxx.

    Args:
        phone (str): telefone sem formatação

    Returns:
        str: telefone formatado
    """
    formated_phone = "+" + phone[0:2] + " (" + phone[2:4] + ") " + phone[4:9] + "-" + phone[9:13]
    return formated_phone
