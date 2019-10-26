import logging
from app import LOG_LEVEL
from app.resources import CashFlow, CashFlowMapping

log = logging.getLogger(__name__)
log.setLevel(LOG_LEVEL)


cash_flow_handler = CashFlow.handler
cash_flow_mapping_handler = CashFlowMapping.handler
