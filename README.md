# Casio ROP Translator Tool web

This tool allows you to translate ROP (Return-Oriented Programming) addresses between supported Casio calculator models.

## How to Use

### 1. Launching the Translator via Local Server

To run the translator, you need a local web server. The `start.py` script simplifies this process.

* **Preparation:** Ensure these files are in the *same directory*:
    * `index.html`
    * `start.py`
    * All supported ROM dump `.txt` files (e.g., `fx991cnx.txt`, `fx580vnx.txt`,...).

* **Steps:**
    1.  Open your terminal or cmd.
    2.  Navigate to the folder containing the files.
    3.  Run the Python script: `python3 start.py`
    4.  A local web server will start (usually on `http://localhost:8000`). Your browser should automatically open `http://localhost:8000/index.html`. If not, open it manually.
    5.  **Keep the terminal/cmd** while using the translator. Close it to stop the server.

### 2. Selecting Translation Models

Once the translator is open in your browser:

* You'll see "Chọn File Dịch Từ" and "Chọn File Dịch Đến" dropdowns.
* Select the models you wish to translate between.

### 3. Entering ROP Data for Translation

* In the "Nhập" field, enter the ROP address to translate.
* Each ROP address should be on a separate line.
* The input format is `Offset:Gadget` (e.g., `2:03D2H`).
* Comments can be added on lines starting with `#`.
* Type `end` on a separate line to stop processing further input.
* Click the "Dịch" button to see results in the "Kết Quả" area.

## Notes

* **Python Requirement:** You need Python installed to run `start.py`.
* **Data File Format:** `.txt` ROM dump files must be correctly formatted.
* **Accuracy:** Translation accuracy depends on gadget similarity. Not 100% guaranteed.
* **Errors:**
    * "Translation not found": Gadget not found in target ROM.
    * "Error: Please run via local server and check files!": Files not loaded correctly (usually due to not running via server).
* **Try it out:** https://luongvantam.github.io/Casio-ROP-Translator-Tool-web/
