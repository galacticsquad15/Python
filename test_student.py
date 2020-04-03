import unittest
import student

class MyTestCase(unittest.TestCase):
    def set_up(self):
        self.the_student = student.Student("Knar", "Robert", "Physics", 4.0)

    def tearDown(self):
        del self.the_student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.the_student.lname, "Knar")
        self.assertEqual(self.the_student.fname, "Robert")
        self.assertEqual(self.the_student.major, "Physics")

    def test_object_created_all_attributes(self):
        self.assertEqual(self.the_student.lname, "Knar")
        self.assertEqual(self.the_student.fname, "Robert")
        self.assertEqual(self.the_student.major, "Physics")
        self.assertEqual(self.the_student.gpa, 4.0)

    def test_student_str(self):
        self.assertEqual(self.the_student.__str__, "Knar, Robert has major Physics with gpa: 4.0")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = student.Student('123', 'Robert', "Physics")

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            p = student.Student("Knar", "123", "Physics")

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            p = student.Student("Knar", "Robert", "123")

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            p = student.Student("Knar", "Robert", "Physics", "123")





if __name__ == '__main__':
    unittest.main()
