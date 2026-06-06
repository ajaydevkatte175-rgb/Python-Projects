import os
import sys
from pypdf import PdfReader, PdfWriter

def clear_screen():
    """Utility to keep the terminal interface clean."""
    os.system('cls' if os.name == 'nt' else 'clear')

def split_pdf_workflow():
    print("\n--- ✂️ PDF SPLITTER MODULE ✂️ ---")
    input_path = input("Enter the path of the PDF file to split: ").strip('" ')
    
    if not os.path.exists(input_path):
        print("❌ Error: File not found! Please check the file path.")
        return

    # Extract directory and base name to save split pages in the same folder
    output_dir = os.path.dirname(input_path)
    base_name = os.path.splitext(os.path.basename(input_path))[0]

    try:
        # Read the source document into memory
        reader = PdfReader(input_path)
        total_pages = len(reader.pages)
        print(f"📖 Loaded '{base_name}.pdf' successfully. Total pages: {total_pages}")

        # Iterate through every page and write it out as a unique file
        for page_num in range(total_pages):
            writer = PdfWriter()
            writer.add_page(reader.pages[page_num])
            
            # Construct naming pattern: filename_page_1.pdf, filename_page_2.pdf...
            output_filename = f"{base_name}_page_{page_num + 1}.pdf"
            full_output_path = os.path.join(output_dir, output_filename)
            
            with open(full_output_path, "wb") as output_file:
                writer.write(output_file)
                
        print(f"✅ Success! Split {total_pages} individual pages inside: {output_dir if output_dir else 'current directory'}")

    except Exception as e:
        print(f"❌ Structural operational failure: {e}")

def encrypt_pdf_workflow():
    print("\n--- 🔒 PDF ENCRYPTION MODULE 🔒 ---")
    input_path = input("Enter the path of the PDF file to protect: ").strip('" ')
    
    if not os.path.exists(input_path):
        print("❌ Error: File not found!")
        return

    password = input("Set your secure PDF opening password: ").strip()
    if not password:
        print("❌ Error: Password cannot be blank!")
        return

    # Construct the output filename
    output_dir = os.path.dirname(input_path)
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_filename = f"{base_name}_protected.pdf"
    full_output_path = os.path.join(output_dir, output_filename)

    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()

        # Clone all pages from the original reader into our new output writer pipeline
        for page in reader.pages:
            writer.add_page(page)

        # Apply the encryption algorithm pass directly onto the writer engine data matrix
        writer.encrypt(password)

        with open(full_output_path, "wb") as output_file:
            writer.write(output_file)
            
        print(f"✅ Success! Secure encrypted file created at:\n👉 {full_output_path}")

    except Exception as e:
        print(f"❌ Encryption routine failure: {e}")

def main_menu():
    while True:
        clear_screen()
        print("=========================================")
        print("    WSCUBE TECH - PDF TOOLKIT ENGINE     ")
        print("=========================================")
        print("1. Split a PDF into Single-Page Files ✂️")
        print("2. Encrypt a PDF with a Password 🔒")
        print("3. Exit System 🚪")
        print("=========================================")
        
        choice = input("Select an option (1-3): ").strip()

        if choice == '1':
            split_pdf_workflow()
            input("\nPress Enter to return to main menu...")
        elif choice == '2':
            encrypt_pdf_workflow()
            input("\nPress Enter to return to main menu...")
        elif choice == '3':
            print("\nShutting down PDF Toolkit. Goodbye!")
            sys.exit()
        else:
            print("\n❌ Invalid choice! Please select 1, 2, or 3.")
            time_delay = input("\nPress Enter to try again...")

if __name__ == "__main__":
    main_menu()