from re import IGNORECASE, compile
from telethon import events
from pyrogram import filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from bot.core.Commands import Commands
from bot.core.handlers.handle_cancel import handle_cancel
from bot.core.handlers.handle_config import handle_config
from bot.core.handlers.handle_copy import handle_copy_command
from bot.core.handlers.handle_mirror import handle_clone_command, handle_mirror_command, handle_qbit_mirror_command, handle_unzip_mirror_command, handle_zip_mirror_command
from bot.core.handlers.handle_exec import handle_exec_message_f
from bot.core.handlers.handle_getlogs import get_logs
from bot.core.handlers.handle_leech import handle_leech_command, handle_unzip_leech_command, handle_zip_leech_command
from bot.core.handlers.handle_myfiles import handle_myfiles
from bot.core.handlers.handle_restart import handle_restart
from bot.core.handlers.handle_server import handle_server_command
from bot.core.handlers.handle_mirrorset import handle_mirrorset_command
from bot.core.handlers.handle_speedtest import speed_handler
from bot.core.handlers.handle_start import start_handler
from bot.core.handlers.handle_status import status_handler
from bot.core.handlers.handle_test import handle_test_command
from bot.core.menus.callbacks.copy_menu_callback import handle_setting_copy_menu_callback
from bot.core.menus.callbacks.leech_menu_callback import handle_leech_menu_callback
from bot.core.menus.callbacks.mirror_menu_callback import handle_mirror_menu_callback
from bot.core.menus.callbacks.mirrorset_menu_callback import handle_setting_mirroset_callback
from bot.core.menus.callbacks.myfiles_menu_callback import handle_setting_myfiles_menu_callback
from bot.core.menus.callbacks.qbitsel_menu_callback import get_confirm
from bot.core.menus.callbacks.nextpage.handle_nextpage_copy_menu_cb import next_page_copy
from bot.core.menus.callbacks.nextpage.handle_nextpage_leech_menu_cb import next_page_leech
from bot.core.menus.callbacks.nextpage.handle_nextpage_mirrorset_menu_cb import next_page_mirrorset
from bot.core.menus.callbacks.nextpage.handle_nextpage_myfiles_menu_cb import next_page_myfiles
from bot.core.handlers import handle_batch, handle_search, handle_leech_st


def add_handlers(bot):
    # PYROGRAM HANDLERS

    mirror_handler = MessageHandler(
        handle_mirror_command,
        filters=filters.command(Commands.MIRROR))
    bot.pyro.add_handler(mirror_handler)

    config_handler = MessageHandler(
        handle_config,
        filters=filters.command(Commands.CONFIG))
    bot.pyro.add_handler(config_handler)

    status_handlers = MessageHandler(
        status_handler,
        filters=filters.command(Commands.STATUS))
    bot.pyro.add_handler(status_handlers)

    zip_mirror_handler = MessageHandler(
        handle_zip_mirror_command,
        filters=filters.command(Commands.ZIPMIRROR))
    bot.pyro.add_handler(zip_mirror_handler)

    unzip_mirror_handler = MessageHandler(
        handle_unzip_mirror_command,
        filters=filters.command(Commands.UNZIPMIRROR))
    bot.pyro.add_handler(unzip_mirror_handler)

    clone_handler = MessageHandler(
        handle_clone_command,
        filters=filters.command(Commands.CLONE))
    bot.pyro.add_handler(clone_handler)

    qbit_handler = MessageHandler(
        handle_qbit_mirror_command,
        filters=filters.command(Commands.QBMIRROR))
    bot.pyro.add_handler(qbit_handler)

    leech_handler = MessageHandler(
        handle_leech_command,
        filters=filters.command(Commands.LEECH))
    bot.pyro.add_handler(leech_handler)

    zip_leech_handler = MessageHandler(
        handle_zip_leech_command,
        filters=filters.command(Commands.ZIPLEECH))
    bot.pyro.add_handler(zip_leech_handler)

    unzip_leech_handler = MessageHandler(
        handle_unzip_leech_command,
        filters=filters.command(Commands.UNZIPLEECH))
    bot.pyro.add_handler(unzip_leech_handler)

    myfiles_handler = MessageHandler(
        handle_myfiles,
        filters=filters.command(Commands.MYFILES))
    bot.pyro.add_handler(myfiles_handler)

    test_handler = MessageHandler(
        handle_test_command,
        filters=filters.command(Commands.TEST))
    bot.pyro.add_handler(test_handler)

    # TELETHON HANDLERS

    bot.add_event_handler(
        handle_copy_command,
        events.NewMessage(pattern=command_process(f"/{Commands.COPY}")))

    bot.add_event_handler(
        handle_exec_message_f,
        events.NewMessage(pattern=command_process(f"/{Commands.EXEC}")))

    bot.add_event_handler(
        handle_restart,
        events.NewMessage(pattern=command_process(f"/{Commands.RESTART}")))

    bot.add_event_handler(
        get_logs,
        events.NewMessage(pattern=command_process(f"/{Commands.GETLOGS}")))

    bot.add_event_handler(
        handle_server_command,
        events.NewMessage(pattern=command_process(f"/{Commands.SERVER}")))

    bot.add_event_handler(
        start_handler,
        events.NewMessage(pattern=command_process(f"/{Commands.START}")))

    bot.add_event_handler(
        speed_handler,
        events.NewMessage(pattern=command_process(f"/{Commands.SPEEDTEST}")))

    bot.add_event_handler(
        handle_mirrorset_command,
        events.NewMessage(pattern=command_process(f"/{Commands.MIRRORSET}")))

    # Callback Handlers

    # next
    bot.add_event_handler(
        next_page_mirrorset,
        events.CallbackQuery(pattern="n_mirrorset"))

    bot.add_event_handler(
        next_page_copy,
        events.CallbackQuery(pattern="n_copy"))

    bot.pyro.add_handler(
        CallbackQueryHandler(
            next_page_myfiles,
            filters=filters.regex("n_myfiles")))

    bot.pyro.add_handler(
        CallbackQueryHandler(
            next_page_leech,
            filters=filters.regex("n_leech")))

    bot.pyro.add_handler(
        CallbackQueryHandler(
            get_confirm,
            filters=filters.regex("btsel")))

    # MENUS
    bot.pyro.add_handler(
        CallbackQueryHandler(
            handle_setting_myfiles_menu_callback,
            filters=filters.regex("myfilesmenu")))

    bot.pyro.add_handler(
        CallbackQueryHandler(
            handle_leech_menu_callback,
            filters=filters.regex("leechmenu")))

    bot.pyro.add_handler(
        CallbackQueryHandler(
            handle_mirror_menu_callback,
            filters=filters.regex("mirrormenu")))

    bot.add_event_handler(
        handle_setting_copy_menu_callback,
        events.CallbackQuery(pattern="copymenu"))

    bot.add_event_handler(
        handle_setting_mirroset_callback,
        events.CallbackQuery(pattern="mirrorsetmenu"))
    
    # others
    bot.add_event_handler(
        handle_cancel,
        events.CallbackQuery(pattern="cancel"))

    bot.add_event_handler(
        handle_server_command,
        events.CallbackQuery(pattern="fullserver"))

def command_process(cmd):
    return compile(cmd, IGNORECASE)
