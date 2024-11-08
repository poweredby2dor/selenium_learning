"""
******************************************************************************
CONFIDENTIAL AND PROPRIETARY

This source code is the property of [Your Company Name] and is provided
under the terms of a Non-Disclosure Agreement (NDA) between [Your Company
Name] and the authorized recipient. Any unauthorized copying, distribution,
modification, or use of this source code is strictly prohibited and may
result in legal action.

© [Year] [Your Company Name]. All rights reserved.
******************************************************************************
"""

import os


def logger(log, msg, send_to_console):
    """
        Logs messages to console and log file
        log (str): input message
        msg (str): input message for console
        return_type: none
    """
    if send_to_console:
        print(msg)

    with open(os.path.join(os.getcwd(), os.pardir, "logs", "execution.log"), 'a', encoding="utf-8") as file:
        file.write(log+"\n")


def info(log="[i1] No info message given to the logger."):
    """
        Prints message with default font color
        log (str): input message
        return_type: none
    """

    logger(log, log, True)


def warning(log="[W1] No warning message given to the logger."):
    """
        Prints message with yellow font color
        msg (str): input message
        return_type: none
    """

    msg = "\033[33m"+log+"\033[0m"
    logger(log, msg, True)


def error(log="[E1] No error message given to the logger."):
    """
        Prints message with red font color
        msg (str): input message
        return_type: none
    """

    msg = "\033[31m"+log+"\033[0m"
    logger(log, msg, True)


def debug(log="[D1] No debug message given to the logger."):
    """
        Prints message with magenta font color
        msg (str): input message
        return_type: none
    """
    msg = "\033[35m"+log+"\033[0m"
    logger(log, msg, False)


def result(log="[R1] No result message given to the logger."):
    """
        Prints message with blue font color
        msg (str): input message
        return_type: none
    """
    msg = "\033[34m"+log+"\033[0m"
    logger(log, msg, True)


# pylint: disable=pointless-string-statement
"""
ANSI Color Codes:

# Text (Foreground) Colors
\033[30m  Black
\033[31m  Red
\033[32m  Green
\033[33m  Yellow
\033[34m  Blue
\033[35m  Magenta
\033[36m  Cyan
\033[37m  White
\033[90m  Bright Black (Gray)
\033[91m  Bright Red
\033[92m  Bright Green
\033[93m  Bright Yellow
\033[94m  Bright Blue
\033[95m  Bright Magenta
\033[96m  Bright Cyan
\033[97m  Bright White

# Background Colors
\033[40m  Black Background
\033[41m  Red Background
\033[42m  Green Background
\033[43m  Yellow Background
\033[44m  Blue Background
\033[45m  Magenta Background
\033[46m  Cyan Background
\033[47m  White Background
\033[100m Bright Black (Gray) Background
\033[101m Bright Red Background
\033[102m Bright Green Background
\033[103m Bright Yellow Background
\033[104m Bright Blue Background
\033[105m Bright Magenta Background
\033[106m Bright Cyan Background
\033[107m Bright White Background

# Reset Color
\033[0m  Reset to default color
"""
