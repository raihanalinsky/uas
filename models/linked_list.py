from models.node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    # ======================
    # tambah node
    # ======================
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    # ======================
    # convert list
    # ======================
    def to_list(self):
        result = []

        current = self.head

        while current:
            result.append(current.data)
            current = current.next

        return result

    # ======================
    # cari barang
    # ======================
    def find(self, kode):
        current = self.head

        while current:

            if str(current.data["Kode"]) == str(kode):
                return current

            current = current.next

        return None

    # ======================
    # cari username
    # ======================
    def find_username(self, username):
        current = self.head

        while current:

            if current.data["Username"] == username:
                return current

            current = current.next

        return None

    # ====================================
    # menghapus berdasarkan key dan value
    # ====================================
    def delete_by_key(self, key, value):
        current = self.head
        prev = None

        while current:
            if str(current.data.get(key)) == str(value):
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next

                return True

            prev = current
            current = current.next
        return False

    # ======================================
    # update node berdasarkan key dan value
    # ======================================
    def update_by_key(self, key, value, new_data):
        current = self.head

        while current:
            if str(current.data.get(key)) == str(value):
                current.data.update(new_data)
                return True
            current = current.next

        return False
