from django.db import models

class Faculty(models.Model):
    help_text = 'Faculty population in a department incl. race, gender'
    
    #defines rank choices (note: acting only for law)
    RANK_CHOICES = (
                    (Professor, "Professor"),
                    (Assc, "Associate Professor"),
                    (Asst, "Assistant Professor"),
                    (Act, "Acting Professor"),
                    )
                    rank = models.CharField(max_length=30,
                                            choices = RANK_CHOICES)

    #defines ethnicity possibilities acc. document
    RACE_CHOICES = (
                (AA, 'African American'),
                (Asian, 'Asian'),
                (Hispanic, 'Hispanic'),
                (NA, 'Native American'),
                (White, 'White'),
                (Unknown, 'Unknown'),
                )
                race = models.CharField(max_length=20,
                                        chioces=RACE_CHOICES,
                                        default=Unknown)

    # gender = BooleanField()
    GENDER_CHOICES = (
                      (m, "Male"),
                      (f, "Female"),
                      #for checking errors
                      (u, "Unknown"),
                      )
    gender = models.Charfield(max_length=7,
                                choices = GENDER_CHOICES,
                                default = u)
                            
    count = DecimalField(max_digits = 5, decimal_places=2)

    department = models.ForeignKey(Department)

class Department(models.Model):
    #optional parent
    dept_name = models.CharField(max_length=50)
    
    #defines hierarchy among depts/schools/colleges i.e. phyiscs -> physical sciences -> colllege of letters and and sciences
    #need Null=True? Docu advises against using for text-based fields
    #also can a class foreign key itself?
    parent = models.ForeignKey(Department, null=True, blank=True)
