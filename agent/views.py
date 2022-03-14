from rest_framework.decorators import api_view
from rest_framework.response import Response
from agent.services.planneragentconn import PlannerAgentConn


@api_view(['GET','POST'])
def sendMsg(request):
    if request.method == 'POST':
        return Response({"Teste"})    
    elif request.method == 'GET':
        p = PlannerAgentConn.sendMessage("Teste")
        return Response({"Teste"})
    
