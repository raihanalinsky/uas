from models.node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    # ======================
    # Tambah Node
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
    # Convert List
    # ======================

    def to_list(self):

        result = []

        current = self.head

        while current:
            result.append(current.data)
            current = current.next

        return result

    # ======================
    # Cari Barang
    # ======================

    def find(self, kode):

        current = self.head

        while current:

            if str(current.data["Kode"]) == str(kode):
                return current

            current = current.next

        return None

    # ======================
    # Cari Username
    # ======================

    def find_username(self, username):

        current = self.head

        while current:

            if current.data["Username"] == username:
                return current

            current = current.next

        return None

    # ======================
    # Hapus Barang
    # ======================

    def delete(self, kode):

        current = self.head
        prev = None

        while current:

            if str(current.data["Kode"]) == str(kode):

                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next

                return True

            prev = current
            current = current.next

        return False

    # ======================
    # Hapus Akun
    # ======================

    def delete_by_username(self, username):

        current = self.head
        prev = None

        while current:

            if current.data["Username"] == username:

                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next

                return True

            prev = current
            current = current.next

        return False
