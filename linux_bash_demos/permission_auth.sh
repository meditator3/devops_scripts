echo "this demonstrates compartmenlising files for groups/users"
echo "group 1: rebels, group 2: empire"
echo "rebels save secret plan in folder only rebel group can access"
echo "and vice versa, empire holds document in their folder only accissble to their group"
echo "------------------------------------------------------------------------------------"
echo "first, create all users and groups, give them all passwords"
adduser rebel1
adduser rebel2
adduser darth_vader
adduser storm_trooper
echo "creating and adding to group(admin)"
addgroup rebels
addgroup empire
addgroup rebel1 rebels
addgroup rebel2 rebels
addgroup darth_vader empire
addgroup storm_trooper empire
echo "switching to rebels"
su rebel1
mkdir hideout
chown rebel1:rebels hideout
cd hideout
touch secret_plan.txt
echo "created secret plan for rebels"
chmod rebel1:rebels secret_plan.txt
echo "now plan and folder of plan only accissble to rebels and not empire"
