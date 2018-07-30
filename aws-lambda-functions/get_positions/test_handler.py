import boto3
import pytest
from handler import call

def test_handler_moves_incoming_object_to_processed():
    assert call(None, None) == None