# Define the installation directory
$installDir = "C:\Users\knr1931\Program Files\algeon"

# Define the 'lib' and 'bin' directories within the installation directory
$libDir = Join-Path -Path $installDir -ChildPath "lib"
$binDir = Join-Path -Path $installDir -ChildPath "bin"

# Function to remove a directory from PATH
Function RemoveDirectoryFromPath($directory, $target) {
    $path = [System.Environment]::GetEnvironmentVariable("PATH", [int]$target)
    if ($path -like "*$directory*") {
        $newPath = $path -replace [regex]::Escape("$directory;"), ""
        [System.Environment]::SetEnvironmentVariable("PATH", $newPath, [int]$target)
        Write-Host "Removed '$directory' directory from the $target PATH."
    }
    else {
        Write-Host "'$directory' directory not found in the $target PATH."
    }
}

# Check if the installation directory exists, and if so, remove it
if (Test-Path $installDir -PathType Container) {
    Write-Host "Removing installation directory: $installDir"
    Remove-Item -Path $installDir -Recurse -Force
}
else {
    Write-Host "Installation directory not found: $installDir"
}

# Remove 'lib' and 'bin' directories from the user's PATH
RemoveDirectoryFromPath $libDir 1 # 1 represents [System.EnvironmentVariableTarget]::User
RemoveDirectoryFromPath $binDir 1 # 1 represents [System.EnvironmentVariableTarget]::User

Write-Host "Uninstallation complete."