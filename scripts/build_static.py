import os
import json
from datetime import datetime, timezone

def build_static_data(items=None, source_date=None, output_path="data.json"):
    """
    Fungsi utama untuk membuat atau memperbarui data.json.
    Script ini TIDAK AKAN menyentuh atau menimpa file index.html.
    """
    # Jika items tidak dioper, coba baca data yang sudah ada di data.json
    if items is None:
        if os.path.exists(output_path):
            try:
                with open(output_path, "r", encoding="utf-8") as f:
                    existing_data = json.load(f)
                    items = existing_data.get("items", [])
                    source_date = source_date or existing_data.get("sourceDate")
            except Exception as e:
                print(f"⚠️ Gagal membaca {output_path} lama: {e}")
                items = []
        else:
            items = []

    # Susun struktur JSON
    payload = {
        "sourceDate": source_date,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "items": items
    }

    # Tulis HANYA ke file data.json
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        print(f"✅ File '{output_path}' berhasil diperbarui!")
        print("🔒 File 'index.html' tetap aman dan tidak diubah.")
    except Exception as e:
        print(f"❌ Gagal menulis file {output_path}: {e}")

def main():
    # Jalankan proses update data
    build_static_data()

if __name__ == "__main__":
    main()
