from django.db import models
import datetime
class Membership(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class PlayerRegistration(models.Model):
    first_name = models.CharField(max_length = 20)
    middle_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    fathers_name = models.CharField(max_length = 20)
    mother_name = models.CharField(max_length = 20)
    present_address = models.CharField(max_length = 30)
    house_no = models.CharField(max_length = 20)
    location = models.CharField(max_length = 20)
    village_Or_street = models.CharField(max_length = 20)
    thana = models.CharField(max_length = 20)
    district = models.CharField(max_length = 20)
    post_code = models.CharField(max_length = 20)
    permanent_address = models.CharField(max_length = 20)
    house_no = models.CharField(max_length = 20)
    location = models.CharField(max_length = 20)
    village_Or_street = models.CharField(max_length = 20)
    thana = models.CharField(max_length = 20)
    district = models.CharField(max_length = 20)
    post_code = models.CharField(max_length = 20)
    date_of_birth = models.DateField(max_length=8)
    previous_club_name = models.CharField(max_length = 20)
    fromm = models.CharField(max_length = 20)
    to = models.CharField(max_length = 20)
    total_runs = models.CharField(max_length = 20)
    total_wickets = models.CharField(max_length = 20)
    team_leader = models.CharField(max_length = 20)
    best_performance_club_name = models.CharField(max_length = 20)
    opponent_club_name = models.CharField(max_length = 20)
    event_id = models.IntegerField()
    match_id = models.IntegerField()
    runs = models.IntegerField()
    wickets = models.IntegerField()
    name_of_degree = models.CharField(max_length = 20)
    institution_OR_department = models.CharField(max_length = 20)
    board_OR_Universty = models.CharField(max_length = 20)
    passing_year = models.IntegerField()
    result = models.CharField(max_length = 10)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
