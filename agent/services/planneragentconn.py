import asyncio
import logging
from typing import Any
from spade.behaviour import OneShotBehaviour
from spade.message import Message
from spade.agent import Agent

logger = logging.getLogger(__name__)

class PlannerAgentConn:

    _agent = None

    @classmethod
    def sendMessage(self, msg : str) -> None:

        if self._agent is None:
            self._agent = ConnAgentMessage("sfdjango@xmpp-server","sfdjango")
        future = self._agent.start(auto_register=True)
        #self._agent.b.join()
        print("Finalizado")
        

class ConnAgentMessage(Agent):
    class SendMsgBehaviour(OneShotBehaviour):
        async def run(self):
            msg = Message(to="ruleragent@xmpp-server")
            msg.set_metadata("performative","inform")
            msg.set_metadata("ontology", "myOntology")
            msg.set_metadata("language","OWL-S")
            msg.body = "SFDJANGO MESSAGE"

            await self.send(msg)
            
            self.exit_code = "Msg sent finalized"
            await self.agent.stop()
    
    async def setup(self):
        self.b = self.SendMsgBehaviour()
        self.add_behaviour(self.b)


