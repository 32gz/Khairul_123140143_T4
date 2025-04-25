class TaskError(Exception):
    
    pass

class InvalidChoiceError(TaskError):
    
    pass

class EmptyTaskError(TaskError):
    
    pass

class TaskNotFoundError(TaskError):
    
    pass

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str):
        
        if not task or not task.strip():
            raise EmptyTaskError("Tugas tidak boleh kosong.")
        self.tasks.append(task.strip())

    def remove_task(self, index: int):
        
        if index < 1 or index > len(self.tasks):
            raise TaskNotFoundError(f"Tugas dengan nomor {index} tidak ditemukan.")
        self.tasks.pop(index - 1)

    def display_tasks(self):
        
        if not self.tasks:
            print("Daftar tugas masih kosong.")
        else:
            print("Daftar Tugas:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")


def main():
    manager = TaskManager()
    actions = {
        1: "Tambah tugas",
        2: "Hapus tugas",
        3: "Tampilkan daftar tugas",
        4: "Keluar"
    }

    while True:
        print("\nPilih aksi:")
        for key, desc in actions.items():
            print(f"{key}. {desc}")
        try:
            choice_input = input("Masukkan pilihan (1/2/3/4): ")
            if not choice_input.isdigit():
                raise InvalidChoiceError("Pilihan harus berupa angka 1, 2, 3, atau 4.")

            choice = int(choice_input)
            if choice not in actions:
                raise InvalidChoiceError("Pilihan tidak valid. Silakan pilih antara 1 hingga 4.")

            if choice == 1:
                task = input("Masukkan tugas yang ingin ditambahkan: ")
                manager.add_task(task)
                print("Tugas berhasil ditambahkan!")

            elif choice == 2:
                index_input = input("Masukkan nomor tugas yang ingin dihapus: ")
                if not index_input.isdigit():
                    raise InvalidChoiceError("Nomor tugas harus berupa angka.")
                index = int(index_input)
                manager.remove_task(index)
                print("Tugas berhasil dihapus!")

            elif choice == 3:
                manager.display_tasks()

            elif choice == 4:
                print("Keluar dari program.")
                break

        except TaskError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan tak terduga: {e}")

if __name__ == "__main__":
    main()
