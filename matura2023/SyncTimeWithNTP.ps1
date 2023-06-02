$NtpServer = "pool.ntp.org"
$TimeService = Get-Service -Name "w32time"
$W32tmPath = "C:\Windows\System32\w32tm.exe"

if ($TimeService.Status -ne "Running") {
    Write-Host "Uruchamianie usługi Windows Time..."
    Start-Service -Name "w32time"
}

Write-Host "Konfiguracja serwera NTP..."
w32tm /config /manualpeerlist:$NtpServer /syncfromflags:MANUAL /reliable:YES /update

Write-Host "Restartowanie usługi Windows Time..."
Restart-Service -Name "w32time"

Write-Host "Synchronizacja czasu..."
& $W32tmPath /resync /force

Write-Host "Sprawdzanie aktualnego czasu..."
& $W32tmPath /query /status
