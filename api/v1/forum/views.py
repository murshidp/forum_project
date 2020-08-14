from .serializers import ForumSerializer,SubforumSerializer,ThreadSerializer,UserSerializer
from forum.models import Forum,Subforum,Thread
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny,IsAuthenticated


def generate_serializer_errors(args):
    message = ""
    for key, values in args.items():
        error_message=""
        for value in values:
            error_message += value + "," 
        error_message=error_message[:-1]

        message +="%s : %s | " %(key,error_message)
    return message[:-3]

@api_view(['GET'])
def forumlist(request):
    forums = Forum.objects.all()
    serializer = ForumSerializer(forums,many=True)
    response_data={
        "StatusCode":6000,
        'data':serializer.data
    }
    return Response(response_data,status=status.HTTP_200_OK)

@api_view(['GET'])
def subforumlist(request,pk):
    forums = Subforum.objects.filter(forum__pk=pk)
    serializer = SubforumSerializer(forums,many=True)
    response_data={
        "StatusCode":6000,
        'data':serializer.data
    }
    return Response(response_data,status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((AllowAny,))
def treadList(request,subforum_id):
    treads = Thread.objects.filter(forum_category__pk=subforum_id)
    serializer=ThreadSerializer(treads,many=True,context={"request":request})
    response_data={
        "StatusCode":6000,
        'data':serializer.data
    }
    return Response(response_data,status=status.HTTP_200_OK)
@api_view(['GET'])
@permission_classes((AllowAny,))
def treadView(request,tread_id):
    try:
        tread = Thread.objects.get(pk=tread_id)
    except Thread.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ThreadSerializer(tread,context={"request":request})
    response_data={
        "StatusCode":6000,
        'data':serializer.data
    }
    return Response(response_data,status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def treadcreate(request,subforum_id):
    serializer = ThreadSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        sub=Subforum.objects.get(pk=subforum_id)
        serializer.save(forum_category=sub)
        response_data={
        "StatusCode":6000,
        'data':serializer.data
        }
        return Response(response_data,status=status.HTTP_200_OK)
    else:
        response_data={
            "StatusCode":6001,
            "message":generate_serializer_errors(serializer._errors)
        }
    return Response(response_data,status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def editThread(request,tread_id):
    
    try:
        instance = Thread.objects.get(pk=tread_id)
        
    except Thread.DoesNotExist:
        response_data={
                "StatusCode":6001,
                "message":"tread not found"
        }
        return Response(response_data,status=status.HTTP_404_NOT_FOUND)
    serializer = ThreadSerializer(instance,data=request.data)
    sub=instance.forum_category
    if serializer.is_valid():
        serializer.save(forum_category=sub)
        response_data={
            "StatusCode":6000,
            'data':serializer.data
            }
        return Response(response_data,status=status.HTTP_200_OK)
    else:
        response_data={
                "StatusCode":6001,
                "message":generate_serializer_errors(serializer._errors)
        }
        return Response(response_data,status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def deleteTread(request,tread_id):
    try:
        instance = Thread.objects.get(pk=tread_id)
        
    except Thread.DoesNotExist:
        response_data={
                "StatusCode":6001,
                "message":"tread not found"
        }
        return Response(response_data,status=status.HTTP_404_NOT_FOUND)
    instance.delete()
    response_data={
            "StatusCode":6003,
            "message":"Deleted"
        }
    return Response(response_data,status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(["POST"])
def signupView(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response_data={
            "StatusCode":6000,
            'data':serializer.data
            }
        return Response(response_data,status=status.HTTP_200_OK)
    else:
        response_data={
                "StatusCode":6001,
                "message":generate_serializer_errors(serializer._errors)
        }
        return Response(response_data,status=status.HTTP_200_OK)




        




