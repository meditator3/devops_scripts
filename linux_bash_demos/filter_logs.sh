echo "this filters with awk logs of authed users"
echo "(see permission and chmod demo script for users)"
echo "we'll take user rebel1 and darth_vader as reference for 2 examples"
echo "this is rebel1 logs:"
echo "===================="
cat /var/log/auth.log |grep rebel1 |tail -20
echo "now rebel1 will show only the messages of rebel1"
echo "================================================"
cat /var/log/auth.log |grep rebel1 |awk '{ print $5, $6, $7 }' | tail -20

echo "this is darth vader logs (only last 20?)"
echo "========================================"
cat /var/log/auth.log |grep darth_vader |tail -20

echo".........................."
echo "show darth vader messages auth only"
echo "==================================="
cat /var/log/auth.log |grep darth_vader |awk '{ print $5, $6, $7}' |tail -20
