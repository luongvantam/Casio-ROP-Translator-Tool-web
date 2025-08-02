# Casio ROP Translator Tool Web

This tool allows you to translate ROP (Return-Oriented Programming) addresses between supported Casio calculator models.

## How to Use

### 1. Select Translation Models

When you open the tool in your browser, you will see two dropdown menus:

* **"Chọn File Dịch Từ"** (Translate From): Select the `disas` file of the source model.
* **"Chọn File Dịch Đến"** (Translate To): Select the `disas` file of the target model.

A disas file must be provided to enable translation (required in `.txt` format).

### 2. Enter ROP Data

* Enter ROP addresses into the "Nhập" (Input) field.
* Each line should follow the format: `Offset:Gadget` (e.g., `2:03D2H`).
* You can add comments by starting a line with `#`.
* Type `end` on a separate line to mark the end of input.
* Click the **"Dịch"** (Translate) button to see results in the "Kết Quả" (Output) area.

## Notes

* **Accuracy:** Translation depends on gadget similarity between models. Not guaranteed to be 100% accurate.
* **Common Errors:**

  * `"Translation not found"`: Gadget not found in target disas file.
  * `"Error: Please run via local server and check files!"`: Usually caused by incorrectly loaded files or browser limitations.

## Try It Out

[Try the web version here](https://luongvantam.github.io/Casio-ROP-Translator-Tool-web/)
