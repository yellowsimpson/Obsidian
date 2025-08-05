from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time

client = RemoteAPIClient()
sim = client.require('sim')

sim.startSimulation()

object_name = '/UR5'
object_handle = sim.getObject(object_name)

print("핸들: ", object_handle)

sim.stopSimulation()