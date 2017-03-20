Apps:- 

UserProfile
Course
landingpage
students
manager






Course Module :- 

-----------------------------------------
Course:- 

id <--> AutoField(primary_key=True)
title  <--> CharField
sub_title <--> CharField
category  <--> CharField(max_length=127, choices=COURSE_CATEGORY_TYPES, default='Programming')
description  <--> TextField
start_date <--> DateField
finish_date  <--> DateField
is_official  <--> BooleanField
status  <--> PositiveSmallIntegerField(default=settings.COURSE_UNAVAILABLE_STATUS)
image  <--> ImageField
students <--> ManyToManyField(Student)
Instrcutor <--> models.ForeignKey(Instrcutor)

def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super(Course, self).delete(*args, **kwargs) # Call the "real" delete() method

def __str__(self):

def is_published(self):

------------------------------------------
Announcement

announcement_id         <-->  AutoField
title					<--> CharField
body					<--> TextField
post_date				<--> DateField
course					<--> ForeignKey(Course)

@classmethod
    def create(cls, course_id, title, body, post_date):
        announcement = cls(course_id=course_id, title=title,
                           body=body, post_date=post_date)
        return announcement
		
-------------------------------------------------

Syllabus

syllabus_id         <--> AutoField
file         		<--> FileField
course        		<--> ForeignKey(Course)


def delete(self, *args, **kwargs):
    if self.file:
        if os.path.isfile(self.file.path):
            os.remove(self.file.path)
    super(Syllabus, self).delete(*args, **kwargs) # Call the "real" delete() method


-------------------------------------------------


FeedBack:-

feedback_id
MARK_CHOICES = (
        (0, '0 Star'),
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )
marks = models.PositiveSmallIntegerField(
        default=0,
        choices=MARK_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
	
text  <--> TextField
date <--> DateTimeField
user <--> ForeignKey(User)














