var host = "spencewenski.com";
if ((window.location.host == host) && (window.location.protocol != "https:")) {
	window.location = window.location.toString().replace(/^http:/, "https:");
}