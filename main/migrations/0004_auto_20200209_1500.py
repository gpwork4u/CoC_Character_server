# Generated by Django 3.0.3 on 2020-02-09 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_character_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='Arcane_Tome_Spell_Artifact',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='Beliefs',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='Build',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='Damage_Bonus',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='Encounters_with_Strange_Entities',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='HP',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='HP_max',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Injuries_Scars',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='LUCK',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='MP',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='MP_max',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Meaningful_Location',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='Personal_Description',
            field=models.TextField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Phobias_Manias',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='SAN',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Significant_People',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Accounting',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Anthropology',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Appraise',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Archaecology',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Art_Craft',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Charm',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Climb',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Credit',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Cthulhu_Mythos',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Disguise',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Dodge',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Drive_auto',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Elev_Repair',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Fast_Talk',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Fighting',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Firearms_HandGun',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Firearms_Rifle',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_First_Aid',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_History',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Intimidate',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Jump',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Language_Other',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Language_Other_c',
            field=models.CharField(default=10, max_length=20),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Language_Owm',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Language_Owm_c',
            field=models.CharField(default=10, max_length=20),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Law',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_LibraryUse',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Listen',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Locksmith',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Mech_Repair',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Medicine',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Natural_World',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Navigate',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Occult',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Op_Hv_Machine',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Persuade',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Pilot',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Pilot_c',
            field=models.CharField(default=10, max_length=20),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Psychoanalysis',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Psychology',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Ride',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Science',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Science_c',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Sleight_of_Hand',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Spot_Hidden',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Stealth',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Survival',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Survival_c',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Swim',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Throw',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Skill_Track',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='Traits',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='Treasured_Possesions',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AlterField(
            model_name='character',
            name='APP',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='character',
            name='Age',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='character',
            name='Birth_Place',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AlterField(
            model_name='character',
            name='CON',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='character',
            name='DEX',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='character',
            name='EDU',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='character',
            name='INT',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='character',
            name='Job',
            field=models.CharField(default=10, max_length=10),
        ),
        migrations.AlterField(
            model_name='character',
            name='MOV',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='character',
            name='Name',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AlterField(
            model_name='character',
            name='POW',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='character',
            name='Residence',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AlterField(
            model_name='character',
            name='SIZ',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='character',
            name='STR',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='character',
            name='Sex',
            field=models.CharField(default=10, max_length=2),
        ),
        migrations.AlterField(
            model_name='character',
            name='account',
            field=models.CharField(default=10, max_length=10),
        ),
        migrations.AlterField(
            model_name='character',
            name='password',
            field=models.CharField(default=10, max_length=10),
        ),
    ]
