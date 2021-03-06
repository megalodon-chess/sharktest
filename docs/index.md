# Sharktest

Programs for testing Megalodon.

## How It Works

Inspired by Stockfish's Fishtest, this is a server-client system that allows
you to use your CPU and test Megalodon parameters.

## How To Use

1. Download the [client][client] Python file (`src/client.py`).

2. You will need Python 3 and packages defined in `requirements.txt`.

3. Run the client file with Python. Follow the setup instructions if this is your first time.
The IP, port, and encryption key are below.

4. You will be asked whether you have a Sharktest key.
If you do, put your key in and jump to step 8. If you don't, keep reading.

5. To prevent fake results, we require all users to solve a CAPTCHA.
Press enter if you would like to continue.

6. Next, choose a path to save a CAPTCHA image. It will be an image of
distorted text.

7. Enter the text in the image and a new key will be generated.
Please save the key somewhere accessible.

8. The client will start playing Megalodon against Megalodon repeatedly.
You can watch the status in the console. Quit any time by pressing Ctrl+C.

## Server IP

**The server is currently not running**

* IP: `54.241.110.86`
* Port: `5269`
* Encryption key: `BW8AFo_TjoTN7N5u00w9xnlMNzp9j0rgabXOwus56GQ=`

[client]: https://github.com/megalodon-chess/sharktest/blob/main/src/client.py
