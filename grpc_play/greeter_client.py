#!/usr/bin/env python3


import logging

import grpc
from protos import play_pb2, play_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = play_pb2_grpc.GreetServiceStub(channel)
        response = stub.Greet(play_pb2.GreetRequest(name="you"))
    print(f"Greeter client received: {response.result}")


if __name__ == "__main__":
    logging.basicConfig()
    run()
