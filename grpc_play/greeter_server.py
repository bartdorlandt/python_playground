#!/usr/bin/env python3
import logging
from concurrent import futures

import grpc
from protos import play_pb2, play_pb2_grpc


class GreetService(play_pb2_grpc.GreetService):
    def Greet(self, request, context):
        return play_pb2.GreetResponse(result=f"Hello, {request.name}")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    play_pb2_grpc.add_GreetServiceServicer_to_server(GreetService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
