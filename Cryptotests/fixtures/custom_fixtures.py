# FIXTURES FOR MAKING CRUD HTTP METHODS
import pytest

from libs.config import Config
from libs.crud_methods import create_, read_, update_, delete_


@pytest.fixture
def config():
    return Config


@pytest.fixture
def create():
    return create_


@pytest.fixture
def read():
    return read_


@pytest.fixture
def update():
    return update_


@pytest.fixture
def delete():
    return delete_
