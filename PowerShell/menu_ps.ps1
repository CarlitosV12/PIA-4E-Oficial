param(
    [int]$op
)

try {
        switch ($op) {
            1 { 
                Write-Host "Ejecutando Revisión de Hashes..."
                Invoke-HashCheck  # Ejecuta la función para revisión de hashes
            }
            2 { 
                Write-Host "Ejecutando Listado de Archivos..."
                Invoke-FileList  # Ejecuta la función para listar archivos
            }
            3 { 
                Write-Host "Ejecutando Revisión de uso de RAM..."
                Invoke-ResourcesSystemMemInfo  # Llama a la función para mostrar el uso de la RAM
            }
            4 { 
                Write-Host "Ejecutando Revisión de uso de Disco..."
                Invoke-ResourcesSystemDiskInfo # Llama a la función para mostrar el uso del disco
            }
            5 { 
                Write-Host "Ejecutando Revisión de uso de CPU..."
                Invoke-ResourcesSystemCPUInfo  # Llama a la función para mostrar el uso del CPU
            }
            6 { 
                Write-Host "Ejecutando Revisión de la Red..."
                Invoke-ResourcesSystemNetInfo  # Llama a la función para mostrar la información de la red
            }
            7 { 
                Write-Host "Ejecutando Auditoría de Permisos de Carpeta..."
                Invoke-AuditFolPer # Ejecuta la auditoría de permisos de la carpeta
            }
            8 { 
                # Opción para ver la ayuda de las funciones
                Write-Host "`nIngrese el número correspondiente a la función para ver la ayuda:"
                Write-Host "[1] Invoke-HashCheck"
                Write-Host "[2] Invoke-FileList"
                Write-Host "[3] Invoke-ResourcesSystemMemInfo"
                Write-Host "[4] Invoke-ResourcesSystemDiskInfo"
                Write-Host "[5] Invoke-ResourcesSystemCPUInfo"
                Write-Host "[6] Invoke-ResourcesSystemNetInfo"
                Write-Host "[7] Invoke-AuditFolPer"
                $helpOption = Read-Host "Ingrese el número de la función para ver la ayuda"
                
                # Muestra la ayuda de la función seleccionada
                switch ($helpOption) {
                    1 { Get-Help Invoke-HashCheck -Full }  # Muestra ayuda completa para revisión de hashes
                    2 { Get-Help Invoke-FileList -Full }   # Muestra ayuda completa para listado de archivos
                    3 { Get-Help Invoke-ResourcesSystemMemInfo -Full }  # Muestra ayuda completa para revisión de uso de RAM
                    4 { Get-Help Invoke-ResourcesSystemDiskInfo -Full } # Muestra ayuda completa para revisión de uso de disco
                    5 { Get-Help Invoke-ResourcesSystemCPUInfo -Full }  # Muestra ayuda completa para revisión de uso de CPU
                    6 { Get-Help Invoke-ResourcesSystemNetInfo -Full }  # Muestra ayuda completa para revisión de la red
                    7 { Get-Help Invoke-AuditFolPer -Full }  # Muestra ayuda completa para auditoría de permisos de carpeta
                    default { Write-Host "Opción de ayuda no válida." -ForegroundColor Red }  # Mensaje de error si la opción no es válida
                }
            }
            9 { 
                Write-Host "Saliendo..."  # Mensaje para salir del script
                break  # Sale del bucle y finaliza el script
            }
            default { 
                Write-Host "Opción no válida. Por favor, seleccione una opción del menú." -ForegroundColor Red }  # Mensaje si la opción ingresada no es válida
        }
    } catch {
        Write-Host "Se produjo un error al ejecutar la opción seleccionada: $_"  # Maneja cualquier error que ocurra al ejecutar la opción
    } finally {
        Write-Host "Proceso completado."  # Mensaje final cuando el script termina
    }
    