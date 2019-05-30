from toscaparser.common.exception import TOSCAException
from toscaparser.utils.gettextutils import _


class FulfillRequirementError(TOSCAException):
    msg_fmt = _('Requirement "%(what)s" could not be fullfilled')


class UnsupportedRequirementError(TOSCAException):
    msg_fmt = _('Requirement "%(what)s" is not supported.')


class UnavailableNodeFilterError (TOSCAException):
    msg_fmt = _('The "%(what)s" requirement support "node_filter" parameter only with "%(param)s" specifying')


class UnsupportedNodeTypeError (TOSCAException):
    msg_fmt = _('Node type "%(what)s" is not supported')


class InappropriateParameterValueError (TOSCAException):
    msg_fmt = _('Assigned value of parameter "%(what)s" is not appropriate. Please change the value')


class UnknownProvider(TOSCAException):
    msg_fmt = _('Provider "%(what)s" is not supported')


class UnspecifiedTranslatorForProviderError(TOSCAException):
    msg_fmt = _('Translator for provider "%(what)s" is not specified')


class UnspecifiedProviderTranslatorForNamespaceError(TOSCAException):
    msg_fmt = _('Translator for namespace "%(what)s" is not specified')


class UnspecifiedFactsParserForProviderError(TOSCAException):
    msg_fmt = _('Ansible facts parser for provider "%(what)s is not specified"')