# Comandos principales de PowerShell 7 y sus contrapartes en Linux/macOS

___

## 1. Navegación del sistema de archivos
### PowerShell
- `Get-Location` → Obtiene el directorio actual.
- `Set-Location <ruta>` → Cambia al directorio especificado.
- `Get-ChildItem` → Lista archivos y carpetas en el directorio actual.

### Linux/macOS
- `pwd` → Muestra el directorio actual (equivalente a `Get-Location`).
- `cd <ruta>` → Cambia al directorio especificado (equivalente a `Set-Location`).
- `ls` → Lista archivos y carpetas (equivalente a `Get-ChildItem`).

---

## 2. Gestión de procesos
### PowerShell
- `Get-Process` → Lista todos los procesos en ejecución.
- `Stop-Process -Name <nombre>` → Detiene un proceso por su nombre.
- `Start-Process <ruta>` → Inicia un proceso o aplicación.

### Linux/macOS
- `ps aux` → Lista todos los procesos en ejecución.
- `kill <PID>` → Termina un proceso por su ID (equivalente a `Stop-Process`).
- `./<archivo>` o `<comando>` → Ejecuta un archivo o comando (equivalente a `Start-Process`).

---

## 3. Gestión de servicios
### PowerShell
- `Get-Service` → Lista todos los servicios del sistema.
- `Start-Service <nombre>` → Inicia un servicio.
- `Stop-Service <nombre>` → Detiene un servicio.

### Linux/macOS
- `systemctl list-units --type=service` → Lista todos los servicios (en sistemas basados en systemd).
- `systemctl start <nombre>` → Inicia un servicio.
- `systemctl stop <nombre>` → Detiene un servicio.

---

## 4. Manipulación de texto
### PowerShell
- `Select-String <patrón>` → Busca un patrón en un archivo o salida.
- `Get-Content <archivo>` → Lee el contenido de un archivo.
- `Set-Content <archivo> -Value <contenido>` → Escribe contenido en un archivo.

### Linux/macOS
- `grep <patrón> <archivo>` → Busca un patrón en un archivo o salida.
- `cat <archivo>` → Muestra el contenido de un archivo (equivalente a `Get-Content`).
- `echo "contenido" > <archivo>` → Escribe contenido en un archivo.

---

## 5. Administración de red
### PowerShell
- `Test-Connection <host>` → Realiza un ping a un host.
- `Get-NetIPAddress` → Muestra las direcciones IP configuradas.
- `Invoke-WebRequest <URL>` → Realiza una solicitud HTTP.

### Linux/macOS
- `ping <host>` → Realiza un ping a un host.
- `ifconfig` o `ip addr` → Muestra las direcciones IP configuradas.
- `curl <URL>` → Realiza una solicitud HTTP.

---

## 6. Variables y entorno
### PowerShell
- `$env:<nombre>` → Accede a variables de entorno.
- `Get-Variable` → Lista todas las variables.
- `Set-Variable -Name <nombre> -Value <valor>` → Define una variable.

### Linux/macOS
- `echo $<nombre>` → Accede a variables de entorno.
- `set` → Lista todas las variables.
- `<nombre>=<valor>` → Define una variable.

---

## 7. Scripting y flujo de control
### PowerShell
- `if (<condición>) { <bloque> }` → Estructura condicional.
- `foreach ($item in $lista) { <bloque> }` → Itera sobre una lista.
- `function <nombre> { <bloque> }` → Define una función.

### Linux/macOS
- `if [ <condición> ]; then <bloque>; fi` → Estructura condicional.
- `for item in $(<comando>); do <bloque>; done` → Itera sobre una lista.
- `function <nombre> { <bloque> }` → Define una función.

---

## 8. Administración de paquetes
### PowerShell
- `Install-Module <nombre>` → Instala un módulo de PowerShell.
- `Update-Module <nombre>` → Actualiza un módulo.
- `Get-Module` → Lista los módulos instalados.

### Linux/macOS
- `apt install <paquete>` (Debian/Ubuntu) o `yum install <paquete>` (RHEL/CentOS) → Instala un paquete.
- `apt update && apt upgrade` → Actualiza los paquetes instalados.
- `dpkg -l` o `rpm -qa` → Lista los paquetes instalados.

---

## 9. Registro del sistema (Windows específico)
### PowerShell
- `Get-EventLog -LogName <nombre>` → Consulta registros del sistema.
- `Clear-EventLog -LogName <nombre>` → Limpia un registro.

### Linux/macOS
- `journalctl` → Consulta registros del sistema (en sistemas basados en systemd).
- `dmesg` → Muestra mensajes del kernel.

---

## 10. Comandos adicionales útiles
### PowerShell
- `Measure-Command { <bloque> }` → Mide el tiempo de ejecución de un bloque de código.
- `Export-Csv <archivo>` → Exporta datos a un archivo CSV.
- `Import-Csv <archivo>` → Importa datos desde un archivo CSV.

### Linux/macOS
- `time <comando>` → Mide el tiempo de ejecución de un comando.
- `awk`, `sed` → Herramientas para manipular texto y exportar datos.
- `csvkit` → Herramienta para trabajar con archivos CSV.