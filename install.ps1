# Define the installation directory
$installDir = "C:\Users\knr1931\Program Files\algeon"

# Define the 'bin' directory within the installation directory
$binDir = Join-Path -Path $installDir -ChildPath "bin"

# Define the 'lib' directory within the installation directory
$libDir = Join-Path -Path $installDir -ChildPath "lib"

# Check if the installation directory exists, and if so, remove it
if (Test-Path $installDir -PathType Container) {
    Write-Host "Removing existing installation directory: $installDir"
    Remove-Item -Path $installDir -Recurse -Force
}

# Run Meson with the install_dir option
Write-Host "Running Meson with install_dir option..."
meson setup --prefix=$installDir --reconfigure build

# Build the project using Meson
Write-Host "Compiling the project..."
meson compile -C build

# Install the project using Meson
Write-Host "Installing the project..."
meson install -C build

# Check if the 'bin' directory is already in the PATH
if ($env:PATH -notlike "*$binDir*") {
    Write-Host "Adding 'bin' directory to PATH..."
    $env:PATH += ";$binDir"
    [System.Environment]::SetEnvironmentVariable("PATH", $env:PATH, [System.EnvironmentVariableTarget]::User)
}

# Check if the 'lib' directory is already in the PATH
if ($env:PATH -notlike "*$libDir*") {
    Write-Host "Adding 'lib' directory to PATH..."
    $env:PATH += ";$libDir"
    [System.Environment]::SetEnvironmentVariable("PATH", $env:PATH, [System.EnvironmentVariableTarget]::User)
}

Write-Host "Installation complete."