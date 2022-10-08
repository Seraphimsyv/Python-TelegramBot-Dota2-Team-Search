from aiogram import Dispatcher

from bot.states import RegistrationState
from bot.states import RandomSearchState
from bot.states import TargetsSearchState

from .cmd_start import cmd_start

from .profile.handler_profile import handler_profile
from .profile.handler_set_active_profile import handler_set_active_profile

from .registration.handler_set_name import handler_set_name
from .registration.handler_set_rate import handler_set_rate
from .registration.handler_set_position import handler_set_position
from .registration.handler_set_description import handler_set_description
from .registration.handler_set_region import handler_set_region
from .registration.handler_confirm import handler_confirm
from .registration.handler_finish import handler_finish

from .search.handler_get_random import handler_get_random
from .search.handler_get_with_targets import handler_get_with_targets

from .targets.handler_set_rate import handler_target_set_rate
from .targets.handler_set_position import handler_target_set_position
from .targets.handler_set_region import handler_target_set_region
from .targets.handler_finish import handler_target_finish

from .teammates.handler_teammate_request import handler_teammate_request
from .teammates.handler_teammates_confirm import handler_teammates_confirm
from .teammates.handler_teammates_decline import handler_teammates_decline
from .teammates.handler_list_teammates import handler_list_teammates


def register_user_handlers(dp: Dispatcher) -> None:
    # Menu
    dp.register_message_handler(cmd_start, commands=['start'], state="*")
    dp.register_callback_query_handler(cmd_start, lambda cb: cb.data == "BACK_TO_MENU", state="*")
    # Profile
    dp.register_callback_query_handler(handler_profile, lambda cb: cb.data == "PROFILE", state="*")
    dp.register_callback_query_handler(handler_set_active_profile, lambda cb: cb.data == "SET_ACTIVE", state="*")
    # Registration
    dp.register_callback_query_handler(handler_set_name, lambda cb: cb.data == "REGISTRATION", state="*")
    dp.register_message_handler(handler_set_rate, state=RegistrationState.name)
    dp.register_message_handler(handler_set_position, state=RegistrationState.rate)
    dp.register_callback_query_handler(handler_set_description, state=RegistrationState.pos)
    dp.register_message_handler(handler_set_region, state=RegistrationState.desc)
    dp.register_callback_query_handler(handler_confirm, state=RegistrationState.region)
    dp.register_callback_query_handler(handler_finish, state=RegistrationState.confirm)
    # Random search 
    dp.register_callback_query_handler(handler_get_random, lambda cb: cb.data == "SEARCH_RANDOM", state="*")
    dp.register_callback_query_handler(handler_get_random, lambda cb: cb.data == "SEARCH_NEXT", state=RandomSearchState.next)
    # Target search
    dp.register_callback_query_handler(handler_get_with_targets, lambda cb: cb.data == "SEARCH_WITH_TARGETS", state="*")
    dp.register_callback_query_handler(handler_get_with_targets, lambda cb: cb.data == "SEARCH_NEXT", state=TargetsSearchState.next)
    # Target set data
    dp.register_message_handler(handler_target_set_rate, commands=['set_targets'], state="*")
    dp.register_callback_query_handler(handler_target_set_rate, lambda cb: cb.data == "SET_TARGETS", state="*")
    dp.register_message_handler(handler_target_set_position, state=TargetsSearchState.rate)
    dp.register_callback_query_handler(handler_target_set_region, state=TargetsSearchState.pos)
    dp.register_callback_query_handler(handler_target_finish, state=TargetsSearchState.region)
    # Teammates handlers
    dp.register_callback_query_handler(handler_teammate_request, lambda cb: cb.data == "ADD_TO_TEAM", state="*")
    dp.register_callback_query_handler(handler_teammates_confirm, lambda cb: 'CONFIRM' in cb.data, state="*")
    dp.register_callback_query_handler(handler_teammates_decline, lambda cb: 'DECLINE' in cb.data, state="*")
    dp.register_callback_query_handler(handler_list_teammates, lambda cb: cb.data == "TEAMMATES_LIST", state="*")