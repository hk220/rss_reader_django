import inject
from .repositories import RSSRepository, RSSTestRepository
from .repository_interfaces import RSSRepositoryInterface


def inject_config(binder):
    binder.bind(RSSRepositoryInterface, RSSRepository())


inject.configure(inject_config)
