from django.db import models

class StudentShiftInfo(models.Model):
    shift_name = models.CharField(max_length=50, blank=False, null=False)
    def __str__(self):
        return self.shift_name

class StudentClassInfo(models.Model):
    class_name = models.CharField(max_length=50, blank=False, null=False)
    class_short_form = models.CharField(max_length=10, blank=False, null=False)
    def __str__(self):
        return self.class_name



class StudentInfo(models.Model):
    roll = models.IntegerField()
    father_name = models.CharField(max_length=50,blank=False,null=False)
    address = models.CharField(max_length=50,blank=False,null=False)
    name = models.CharField(max_length=50,blank=False,null=False)
    age = models.IntegerField(blank=False,null=False)
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = models.CharField(choices=gender_choice, max_length=6,blank=False,null=False)

    def __str__(self):
        return self.name
class StudentDetailInfo(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    std_class = models.ForeignKey(StudentClassInfo, on_delete=models.CASCADE)
    std_shift = models.ForeignKey(StudentShiftInfo, on_delete=models.CASCADE)
    std_section = models.CharField(max_length=50,blank=False,null=False)
    session  = models.IntegerField(blank=False,null=False)

    def __str__(self):
        return self.student.name
# api module
class AttandaceManager(models.Manager):
    def create_attendance(self,std_cls,std_roll):
        std_obj = StudentDetailInfo.objects.get(student__roll=std_roll, std_class__class_short_form=std_cls)
        at_obj = Attendance.objects.create(student=std_obj, status=1)
        return at_obj


class Attendance(models.Model):
    student = models.ForeignKey(StudentDetailInfo,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)

    objects = AttandaceManager()
    class Meta:
        unique_together = ['student','date']
    def __str__(self):
        return str(self.student.student.roll)
class Result(models.Model):
    board = models.CharField(max_length=10)
    roll = models.IntegerField()
    gpa = models.IntegerField()
    def __str__(self):
        return str(self.roll)