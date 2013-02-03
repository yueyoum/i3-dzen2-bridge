general {
        output_format = "dzen2"
        colors = true
        interval = 2
}

#order += "ipv6"
order += "disk /"
#order += "run_watch DHCP"
#order += "run_watch VPN"
order += "wireless wlan0"
order += "ethernet eth0"
order += "volume master"
order += "battery 1"
order += "cpu_usage"
order += "cpu_temperature 0"
order += "load"
order += "time"


wireless wlan0 {
        format_up = "_W: (%quality at %essid) %ip"
        format_down = "_W: down"
}

ethernet eth0 {
        # if you use %speed, i3status requires root privileges
        format_up = "_E: %ip (%speed)"
	    format_down = "_E: down"
}

battery 1 {
        format = "_B %status %percentage %remaining"
}

run_watch DHCP {
        pidfile = "/var/run/dhclient*.pid"
}

run_watch VPN {
        pidfile = "/var/run/vpnc/pid"
}

time {
	format = "%Y-%m-%d %H:%M:%S"
}

load {
	format = "_L: %1min %5min"
}

cpu_temperature 0 {
	format = "_T: %degrees °C"
}

cpu_usage {
    format = "_U: %usage"
}

disk "/" {
	format = "%free %total"
}

volume master {
    format = "_V: %volume"
    device = "default"
    mixer = "Master"
    mixer_idx = 0
}
