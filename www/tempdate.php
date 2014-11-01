<html>
	<head>
		<title>Home temperature monitor</title>
		<meta http-equiv="refresh" content="60">
	</head>
	<body>
	<?php
		$f = fopen("/var/www/temp.txt","r") or die ("unable to open file");
		echo "Temperature " . fgets($f) . "&deg;c  last checked at " . fgets($f);
		fclose ($f);
	?>
	</body>
</html>
