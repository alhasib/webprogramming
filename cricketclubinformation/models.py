from django.db import models
import datetime
class Membership(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class PlayerRegistration(models.Model):
    first_name = models.CharField(max_length = 20, blank=True, null= True)
    middle_name = models.CharField(max_length = 20, blank=True, null= True)
    last_name = models.CharField(max_length = 20, blank=True, null= True)
    fathers_name = models.CharField(max_length = 20, blank=True, null= True)
    mother_name = models.CharField(max_length = 20, blank=True, null= True)
    present_address = models.CharField(max_length = 30, blank=True, null= True)
    house_no = models.CharField(max_length = 20, blank=True, null= True)
    location = models.CharField(max_length = 20, blank=True, null= True)
    street = models.CharField(max_length = 20, blank=True, null= True)
    thana = models.CharField(max_length = 20, blank=True, null= True)
    district = models.CharField(max_length = 20, blank=True, null= True)
    post_code = models.CharField(max_length = 20, blank=True, null= True)
    permanent_address = models.CharField(max_length = 20, blank=True, null= True)
    permanent_house_no = models.CharField(max_length = 20, blank=True, null= True)
    permanent_location = models.CharField(max_length = 20, blank=True, null= True)
    permanent_street = models.CharField(max_length = 20, blank=True, null= True)
    permanent_thana = models.CharField(max_length = 20, blank=True, null= True)
    permanent_district = models.CharField(max_length = 20, blank=True, null= True)
    permanent_post_code = models.CharField(max_length = 20, blank=True, null= True)
    date_of_birth = models.DateField(max_length=8, blank=True, null= True)
    previous_club_name = models.CharField(max_length = 20, blank=True, null= True)
    fromm = models.CharField(max_length = 20, blank=True, null= True)
    to = models.CharField(max_length = 20, blank=True, null= True)
    total_runs = models.CharField(max_length = 20, blank=True, null= True)
    total_wickets = models.CharField(max_length = 20, blank=True, null= True)
    team_leader = models.CharField(max_length = 20, blank=True, null= True)
    best_performance_club_name = models.CharField(max_length = 20, blank=True, null= True)
    opponent_club_name = models.CharField(max_length = 20, blank=True, null= True)
    event_id = models.IntegerField(blank=True, null= True)
    match_id = models.IntegerField(blank=True, null= True)
    runs = models.IntegerField(blank=True, null= True)
    wickets = models.IntegerField(blank=True, null= True)
    name_of_degree = models.CharField(max_length = 20, blank=True, null= True)
    institution = models.CharField(max_length = 20, blank=True, null= True)
    board = models.CharField(max_length = 20, blank=True, null= True)
    passing_year = models.IntegerField(blank=True, null= True)
    result = models.CharField(max_length = 10, blank=True, null= True)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Contact(models.Model):
    club_id = models.IntegerField(blank=True, null= True)
    club_name = models.CharField(max_length = 20, blank=True, null= True)
    first_name = models.CharField(max_length = 20, blank=True, null= True)
    middle_name = models.CharField(max_length = 20, blank=True, null= True)
    last_name = models.CharField(max_length = 20, blank=True, null= True)
    player_id = models.IntegerField(blank=True, null= True)
    authorized_Person_first_name = models.CharField(max_length = 20, blank=True, null= True)
    authorized_Person_middle_name = models.CharField(max_length = 20, blank=True, null= True)
    authorized_Person_last_name = models.CharField(max_length = 20, blank=True, null= True)
    designation = models.CharField(max_length = 20, blank=True, null= True)
    contract_period_start_date = models.DateTimeField(blank=True, null= True)
    contract_period_end_date = models.DateField(blank=True, null= True)
    contract_amount = models.IntegerField(blank=True, null= True)
    payment_serial_number = models.IntegerField(blank=True, null= True)
    payment_due_date = models.DateField(blank=True, null= True)
    payment_date = models.DateField(blank=True, null= True)
    payment_amount = models.IntegerField(blank=True, null= True)
    contract_witness = models.CharField(max_length = 20, blank=True, null= True)

    def __str__(self):
        return str(self.club_id)


class ClubRegistratoin(models.Model):
    club_name = models.CharField(max_length = 20, blank=True, null= True)
    date_of_establishment = models.DateField(blank=True, null= True)
    house_no = models.CharField(max_length = 20, blank=True, null= True)
    location = models.CharField(max_length = 20, blank=True, null= True)
    street = models.CharField(max_length = 20, blank=True, null= True)
    thana = models.CharField(max_length = 20, blank=True, null= True)
    district = models.CharField(max_length = 20, blank=True, null= True)
    post_code = models.CharField(max_length = 20, blank=True, null= True)
    president_name = models.CharField(max_length = 20, blank=True, null= True)

    def __str__(self):
        return str(self.club_name)



class PlayersPerformance(models.Model):
    match_id = models.IntegerField(blank=True, null= True)
    venue_id = models.IntegerField(blank=True, null= True) 
    date_of_the_match = models.DateField(blank=True, null= True)
    player_id = models.IntegerField(blank=True, null= True)
    total_wickets = models.IntegerField(blank=True, null= True)
    total_runs = models.IntegerField(blank=True, null= True)       
    out_standing_performance = models.CharField(max_length = 20, blank=True, null= True)

    def __str__(self):
        return str(self.match_id)

class MatchInformation(models.Model):
    event_id =  models.IntegerField(blank=True, null= True)
    venue_id = models.IntegerField(blank=True, null= True) 
    date_of_the_match = models.DateField(blank=True, null= True)
    match_id = models.IntegerField(blank=True, null= True)
    man_of_the_match = models.CharField(max_length = 20, blank=True, null= True)
    umpires = models.CharField(max_length = 20, blank=True, null= True)

    def __str__(self):
        return str(self.event_id)

class TeamInformation(models.Model):
    club_id = models.IntegerField(blank=True, null= True)
    player_id = models.IntegerField(blank=True, null= True)
    team_formation_date = models.DateField(blank=True, null= True)
    event_id =  models.IntegerField(blank=True, null= True)
    team_leader_id = models.IntegerField(blank=True, null= True)
    team_ledar_name = models.CharField(max_length = 20, blank=True, null= True)
    coach_id = models.IntegerField(blank=True, null= True)
    coach_name = models.CharField(max_length = 20, blank=True, null= True)
    playr_id = models.IntegerField(blank=True, null= True)
    player_name = models.CharField(max_length = 20, blank=True, null= True)



    def __str__(self):
        return str(self.club_id)

