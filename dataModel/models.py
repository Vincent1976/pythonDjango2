from django.db import models

# Create your models here.

class Employee(models.Model):
    EmpId= models.CharField(max_length=20,null=False)
    Password= models.CharField(max_length=100,null=False)
    EmpName= models.CharField(max_length=20,null=False)
    DepartId= models.CharField(max_length=50,null=False)
    Mail= models.CharField(max_length=50,null=False)
    ActionFlg= models.IntegerField(null=False)
    EmpNameEN= models.CharField(max_length=50,null=True)
    Ext= models.CharField(max_length=50,null=True)
    HomePhone= models.CharField(max_length=20,null=True)
    CellPhone= models.CharField(max_length=20,null=True)
    isCellPhonePublic= models.CharField(max_length=50,null=True)
    PersonalPhoto= models.CharField(max_length=500,null=True)
    Sex= models.CharField(max_length=50,null=True)
    Marriage= models.CharField(max_length=50,null=True)
    Birthday= models.CharField(max_length=20,null=True)
    BirthPlace= models.CharField(max_length=100,null=True)
    HouseHold= models.CharField(max_length=100,null=True)
    HomeAddress= models.CharField(max_length=100,null=True)
    University= models.CharField(max_length=50,null=True)
    Major= models.CharField(max_length=50,null=True)
    Degree= models.CharField(max_length=50,null=True)
    GraduationTime= models.CharField(max_length=20,null=True)
    FatherName= models.CharField(max_length=20,null=True)
    FatherYear= models.CharField(max_length=20,null=True)
    MotherName= models.CharField(max_length=20,null=True)
    MotherYear= models.CharField(max_length=20,null=True)
    ParentAddress= models.CharField(max_length=100,null=True)
    ParentTel= models.CharField(max_length=20,null=True)
    Mate= models.CharField(max_length=50,null=True)
    Children= models.CharField(max_length=50,null=True)
    UrgentContact= models.CharField(max_length=50,null=True)
    IDNumber= models.CharField(max_length=50,null=True)
    LiveNumber= models.CharField(max_length=50,null=True)
    PassportNo= models.CharField(max_length=50,null=True)
    SalaryID= models.CharField(max_length=50,null=True)
    FundID= models.CharField(max_length=50,null=True)
    SocialID= models.CharField(max_length=50,null=True)
    EntryDate= models.CharField(max_length=20,null=True)
    regularization= models.CharField(max_length=20,null=True)
    SignDate= models.CharField(max_length=20,null=True)
    ResignDate= models.CharField(max_length=20,null=True)
    CreateDate= models.CharField(max_length=20,null=True)
    CreateUserID= models.CharField(max_length=20,null=True)
    UpdateUserID= models.CharField(max_length=20,null=True)
    UpdateDate= models.CharField(max_length=20,null=True)
    PD= models.CharField(max_length=20,null=True)
    Vocation= models.CharField(max_length=50,null=True)
    MV= models.CharField(max_length=50,null=True)
    Grade= models.CharField(max_length=50,null=True)
    Title= models.CharField(max_length=50,null=True)
    DocSpace= models.IntegerField(null=True)
    TimeSheetAlarm= models.CharField(max_length=50,null=True)
    FavoriteProjects= models.CharField(max_length=1000,null=True)
    ValidFrom= models.CharField(max_length=50,null=True)
    ValidTo= models.CharField(max_length=50,null=True)
    CalendarList= models.CharField(max_length=4,null=True)
    COSTLEVEL= models.CharField(max_length=50,null=True)
    ergentPerson= models.CharField(max_length=50,null=True)
    ergentConnect= models.CharField(max_length=100,null=True)
    ergentRelation= models.CharField(max_length=50,null=True)
    ergentConnect2= models.CharField(max_length=50,null=True)
    TEAMID= models.CharField(max_length=50,null=True)
    SUBCOSTLEVEL= models.CharField(max_length=50,null=True)
    wx_unionid= models.CharField(max_length=100,null=True)
    JL= models.CharField(max_length=500,null=True)
    PostCode= models.CharField(max_length=50,null=True)
    SSGS= models.CharField(max_length=50,null=True)
    LDGX= models.CharField(max_length=50,null=True)
    NHCount= models.CharField(max_length=50,null=True)
    PeopleCount= models.CharField(max_length=50,null=True)
    CheckInOutExcept= models.CharField(max_length=50,null=True)
    BizDepart= models.CharField(max_length=50,null=True)

    