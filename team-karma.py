#!env python
from launchpadlib.launchpad import Launchpad
from argparse import ArgumentParser

'''
Get all members of a team and all sub-teams.
Returns a set of Person names
'''
def get_team_members(lp, team):
    
    _get_team_members_done = [] # Cache of already fetched Launchpad teams
    if team in _get_team_members_done: # Don't fetch team members multiple times
        return set()

    _get_team_members_done.append(team)
    team = lp.people[team]
    members = set()

    for member in team.members:
        if not member.is_team:
            members.add(member.name)
            print ("%d,\"%s\",https://launchpad.net/~%s" % (member.karma, member.display_name, member.name))
        else: # Recurs into sub-teams
            members.update(get_team_members(lp, member.name))

    return members

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("team", help="Luanchpad team name.")
    args = parser.parse_args()
    lp = Launchpad.login_anonymously('Ubuntu Karma Ranking Script', service_root='production', version='1.0')
    members = get_team_members(lp, args.team)
