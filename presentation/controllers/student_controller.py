from usecases.student_usecase import StudentUseCase
from presentation.views.student_view import StudentView


class StudentController:
    def __init__(self, usecase: StudentUseCase, view: StudentView):
        self.usecase = usecase
        self.view = view
        self.view.set_controller(self)

    def load_students(self):
        students = self.usecase.list_students()
        self.view.display_students(students)

    def add_student(self):
        try:
            nim, nama, prodi, angkatan = self.view.get_inputs()

            self.usecase.create_student(
                nim, nama, prodi, angkatan
            )

            self.view.show_info(
                "Sukses",
                "Data mahasiswa berhasil ditambahkan!"
            )

            self.view.clear_inputs()
            self.load_students()

        except Exception as e:
            self.view.show_error("Error", str(e))

    def update_student(self):
        try:
            nim, nama, prodi, angkatan = self.view.get_inputs()

            self.usecase.update_student(
                nim, nama, prodi, angkatan
            )

            self.view.show_info(
                "Sukses",
                "Data mahasiswa berhasil diubah!"
            )

            self.view.clear_inputs()
            self.load_students()

        except Exception as e:
            self.view.show_error("Error", str(e))

    def delete_student(self):
        try:
            nim, _, _, _ = self.view.get_inputs()

            if self.usecase.delete_student(nim):
                self.view.show_info(
                    "Sukses",
                    "Data mahasiswa berhasil dihapus!"
                )

                self.view.clear_inputs()
                self.load_students()

        except Exception as e:
            self.view.show_error("Error", str(e))