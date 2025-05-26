# Translator-ROP-web

This tool allows you to translate ROP (Return-Oriented Programming) addresses between supported Casio calculator models.

## How to Use

### 1. Launching the Translator via Local Server

To run the translator, you need a local web server. The `start.py` script simplifies this process.

* **Preparation:** Ensure these files are in the *same directory*:
    * `translator_rop.html`
    * `start.py`
    * All supported ROM dump `.txt` files (e.g., `fx991cnx.txt`, `fx580vnx.txt`,...).

* **Steps:**
    1.  Open your terminal or command prompt.
    2.  Navigate to the folder containing the files.
    3.  Run the Python script: `python3 start.py`
    4.  A local web server will start (usually on `http://localhost:8000`). Your browser should automatically open `http://localhost:8000/translator_rop.html`. If not, open it manually.
    5.  **Keep the terminal/command prompt open** while using the translator. Close it to stop the server.

### 2. Selecting Translation Models

Once the translator is open in your browser:

* You'll see "Choose Source Translation Model" and "Choose Target Translation Model" dropdowns.
* Select the models you wish to translate between.

### 3. Entering ROP Data for Translation

* In the "Input" text area, enter the ROP addresses to translate.
* Each ROP address should be on a separate line.
* Input format can be `Offset:Gadget` (e.g., `1:7B34H`).
* Comments can be added on lines starting with `#`.
* Type `end` on a separate line to stop processing further input.
* Click the "Translate" button to see results in the "Result" area.

## Important Notes & Licensing

* **Python Requirement:** You need Python installed to run `start.py`.
* **Data File Format:** `.txt` ROM dump files must be correctly formatted.
* **Accuracy:** Translation accuracy depends on gadget similarity. Not 100% guaranteed.
* **Errors:**
    * "Translation not found": Gadget not found in target ROM.
    * "Error: Please run via local server and check files!": Files not loaded correctly (usually due to not running via server).
* This project is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
