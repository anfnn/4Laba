import requests

API_URL = "http://localhost:8000"

def get_tokennnn():
    return input("С‚РѕРєРµРЅ: ")

def create_note():
    token = get_tokennnn()
    text = input("Р’РІРµРґРёС‚Рµ С‚РµРєСЃС‚ Р·Р°РјРµС‚РєРё: ")
    response = requests.post(f"{API_URL}/notes/", json={"text": text}, params={"token": token})
    if response.status_code == 200:
        print(f"Р—Р°РјРµС‚РєР° СЃРѕР·РґР°РЅР° СЃ ID: {response.json()['id']}")
    else:
        print(f"РћС€РёР±РєР°: {response.json()['detail']}")


def get_note():
    token = get_tokennnn()
    note_id = input("Р’РІРµРґРёС‚Рµ ID Р·Р°РјРµС‚РєРё: ")
    response = requests.get(f"{API_URL}/notes/{note_id}", params={"token": token})
    if response.status_code == 200:
        print(f"Р—Р°РјРµС‚РєР° {note_id}: {response.json()['text']}")
    else:
        print(f"РћС€РёР±РєР°: {response.json()['detail']}")


def list_notes():
    token = get_tokennnn()
    response = requests.get(f"{API_URL}/notes/", params={"token": token})
    if response.status_code == 200:
        notes = response.json()['notes']
        if notes:
            print("РЎРїРёСЃРѕРє Р·Р°РјРµС‚РѕРє:")
            for note_id in notes:
                print(f"Р—Р°РјРµС‚РєР° ID: {note_id}")
        else:
            print("Р—Р°РјРµС‚РєРё РѕС‚СЃСѓС‚СЃС‚РІСѓСЋС‚.")
    else:
        print(f"РћС€РёР±РєР°: {response.json()['detail']}")


def delete_note():
    token = get_tokennnn()
    note_id = input("Р’РІРµРґРёС‚Рµ ID Р·Р°РјРµС‚РєРё РґР»СЏ СѓРґР°Р»РµРЅРёСЏ: ")
    response = requests.delete(f"{API_URL}/notes/{note_id}", params={"token": token})
    if response.status_code == 200:
        print(f"Р—Р°РјРµС‚РєР° {note_id} СѓРґР°Р»РµРЅР°.")
    else:
        print(f"РћС€РёР±РєР°: {response.json()['detail']}")

def get_note_info():
    token = get_tokennnn()
    note_id = input("Р’РІРµРґРёС‚Рµ ID Р·Р°РјРµС‚РєРё РґР»СЏ РїРѕР»СѓС‡РµРЅРёСЏ РёРЅС„РѕСЂРјР°С†РёРё: ")
    response = requests.get(f"{API_URL}/notes/{note_id}/info", params={"token": token})
    if response.status_code == 200:
        info = response.json()
        print(f"РРЅС„РѕСЂРјР°С†РёСЏ Рѕ Р·Р°РјРµС‚РєРµ {note_id}:")
        print(f"РЎРѕР·РґР°РЅР°: {info['created_at']}")
        print(f"РћР±РЅРѕРІР»РµРЅР°: {info['updated_at']}")
    else:
        print(f"РћС€РёР±РєР°: {response.json()['detail']}")

def update_note():
    token = get_tokennnn()
    note_id = input("Р’РІРµРґРёС‚Рµ ID Р·Р°РјРµС‚РєРё РґР»СЏ РѕР±РЅРѕРІР»РµРЅРёСЏ: ")
    new_text = input("Р’РІРµРґРёС‚Рµ РЅРѕРІС‹Р№ С‚РµРєСЃС‚ Р·Р°РјРµС‚РєРё: ")
    response = requests.patch(f"{API_URL}/notes/{note_id}", json={"text": new_text}, params={"token": token})
    if response.status_code == 200:
        print(f"Р—Р°РјРµС‚РєР° {note_id} РѕР±РЅРѕРІР»РµРЅР°.")
    else:
        print(f"РћС€РёР±РєР°: {response.json()['detail']}")


def main():
    while True:
        print("\n1. РЎРѕР·РґР°С‚СЊ Р·Р°РјРµС‚РєСѓ")
        print("2. РџРѕР»СѓС‡РёС‚СЊ Р·Р°РјРµС‚РєСѓ РїРѕ ID")
        print("3. РџРѕР»СѓС‡РёС‚СЊ СЃРїРёСЃРѕРє РІСЃРµС… Р·Р°РјРµС‚РѕРє")
        print("4. РЈРґР°Р»РёС‚СЊ Р·Р°РјРµС‚РєСѓ")
        print("5. РџРѕР»СѓС‡РёС‚СЊ РёРЅС„РѕСЂРјР°С†РёСЋ Рѕ Р·Р°РјРµС‚РєРµ")
        print("6. РћР±РЅРѕРІРёС‚СЊ РёРЅС„РѕСЂРјР°С†РёСЋ Рѕ Р·Р°РјРµС‚РєРµ")

        choice = input("->: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            get_note()
        elif choice == "3":
            list_notes()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            get_note_info()
        elif choice == "6":
            update_note()

if __name__ == "__main__":
    main()