import threading

from runtime.java.listener import JavaListener
from runtime.session import Session
from runtime.session_manager import SessionManager

from core.logger import Logger


HOST = "0.0.0.0"
PORT = 25565


logger = Logger()


def run_session(session, session_manager):
    """
    Run one session and remove it from the manager
    when the connection finishes.
    """

    try:

        session.start()

    finally:

        session_manager.remove(
            session
        )

        logger.log(
            f"Active sessions: {session_manager.count()}"
        )



def main():

    answer = input("Log? (Y/N)\n> ")

    if answer == "Y":
        logger.enable()
        print(
            "Logging enabled..."
        )
    else:
        print(
            "Logging disabled."
        )

    logger.log("")
    logger.log("==============================")
    logger.log("      Java2Bedrock Runtime")
    logger.log("==============================")
    logger.log("")


    listener = JavaListener(
        HOST,
        PORT
    )


    session_manager = SessionManager()

    session_counter = 0


    listener.start()


    logger.log(
        f"Java listener started on {HOST}:{PORT}"
    )


    try:

        while True:

            connection = listener.accept()

            session_counter += 1

            address = connection.address


            logger.log("")

            logger.log(
                "========================================"
            )

            logger.log(
                f" Session #{session_counter}"
            )

            logger.log(
                f" Client: {address[0]}:{address[1]}"
            )

            logger.log(
                "========================================"
            )

            logger.log("")


            session = Session(
                connection,
                address,
                logger
            )


            session.session_id = session_counter


            session_manager.add(
                session
            )


            logger.log(
                f"Active sessions: {session_manager.count()}"
            )


            thread = threading.Thread(
                target=run_session,
                args=(
                    session,
                    session_manager
                ),
                daemon=True
            )


            thread.start()


    except KeyboardInterrupt:

        logger.log("")
        logger.log(
            "Stopping Java2Bedrock..."
        )


    finally:

        listener.stop()


        sessions = session_manager.all()


        for session in sessions:

            session.stop()




        logger.log(
            "Runtime stopped."
        )


        logger.close()



if __name__ == "__main__":
    main()
