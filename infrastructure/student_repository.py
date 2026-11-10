from domain.entities import Mahasiswa
from infrastructure.database import Database


class StudentRepository:
    def __init__(self, db: Database):
        self.db = db

    def get_all(self):
        conn = self.db.get_connection()

        if not conn:
            return []

        cursor = conn.cursor()
        query = "SELECT nim, nama, prodi, angkatan FROM mahasiswa"
        cursor.execute(query)

        rows = cursor.fetchall()
        conn.close()

        return [
            Mahasiswa(nim=r[0], nama=r[1], prodi=r[2], angkatan=r[3])
            for r in rows
        ]

    def add(self, mhs: Mahasiswa):
        conn = self.db.get_connection()

        if not conn:
            return False

        cursor = conn.cursor()
        query = """
            INSERT INTO mahasiswa (nim, nama, prodi, angkatan)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (mhs.nim, mhs.nama, mhs.prodi, mhs.angkatan)
        )

        conn.commit()
        conn.close()

        return True

    def update(self, mhs: Mahasiswa):
        conn = self.db.get_connection()

        if not conn:
            return False

        cursor = conn.cursor()
        query = """
            UPDATE mahasiswa
            SET nama=%s, prodi=%s, angkatan=%s
            WHERE nim=%s
        """

        cursor.execute(
            query,
            (mhs.nama, mhs.prodi, mhs.angkatan, mhs.nim)
        )

        conn.commit()
        conn.close()

        return True

    def delete(self, nim: str):
        conn = self.db.get_connection()

        if not conn:
            return False

        cursor = conn.cursor()
        query = "DELETE FROM mahasiswa WHERE nim=%s"

        cursor.execute(query, (nim,))

        conn.commit()
        conn.close()

        return True