﻿#
# Manifiesto del módulo 'Au_Fold'
#
# Generado por Carlos Alexis Vargas Flores
#
# Generado el 16/09/2024
#

@{

# Módulo de script o archivo de módulo binario asociado con este manifiesto.
RootModule = 'Au_Fold.psm1'

# Número de versión de este módulo.
ModuleVersion = '1.0.0'

# PSEditions compatibles
# CompatiblePSEditions = @()

# Id. usado para identificar de forma única este módulo.
GUID = '65ae1a3b-3eca-4b4e-906b-8536b5ee2874'

# Autor de este módulo.
Author = 'Carlos Alexis Vargas Flores'

# Compañía o proveedor de este módulo.
CompanyName = 'Facultad de Ciencias Físico Matemáticas'

# Instrucción de copyright de este módulo.
Copyright = '(c) 2024 Carlos Alexis Vargas Flores. Todos los derechos reservados.'

# Descripción de la funcionalidad proporcionada por este módulo.
Description = 'Este módulo contiene funciones para auditar permisos de seguridad en archivos y carpetas, identificando permisos inseguros que puedan otorgar a usuarios como ''Everyone'' o ''BUILTIN\Users'' acceso excesivo, y proporcionando alertas sobre configuraciones potencialmente riesgosas.'

# Versión mínima del motor de Windows PowerShell requerida por este módulo.
# PowerShellVersion = ''

# El nombre del host de Windows PowerShell requerido por este módulo.
# PowerShellHostName = ''

# Versión mínima del host de Windows PowerShell requerida por este módulo.
# PowerShellHostVersion = ''

# Versión mínima de Microsoft .NET Framework requerida por este módulo. Este requisito previo únicamente es válido para la edición de escritorio de PowerShell.
# DotNetFrameworkVersion = ''

# Versión mínima de Common Language Runtime (CLR) requerida por este módulo. Este requisito previo únicamente es válido para la edición de escritorio de PowerShell.
# CLRVersion = ''

# Arquitectura de procesador (None, X86, Amd64) que requiere este módulo
# ProcessorArchitecture = ''

# Módulos que se deben importar en el entorno global antes de importar este módulo.
# RequiredModules = @()

# Ensamblados que se deben cargar antes de importar este módulo.
# RequiredAssemblies = @()

# Archivos de script (.ps1) que se ejecutan en el entorno del llamador antes de importar este módulo.
# ScriptsToProcess = @()

# Archivos de tipo (.ps1xml) que se van a cargar al importar este módulo.
# TypesToProcess = @()

# Archivos de formato (.ps1xml) que se van a cargar al importar este módulo.
# FormatsToProcess = @()

# Módulos para importar como módulos anidados del módulo especificado en RootModule/ModuleToProcess
# NestedModules = @()

# Funciones para exportar desde este módulo; para conseguir el mejor rendimiento, no uses caracteres comodines ni elimines la entrada; usa una matriz vacía si no hay funciones que exportar.
FunctionsToExport = '*'

# Cmdlets para exportar desde este módulo; para conseguir el mejor rendimiento, no uses caracteres comodines ni elimines la entrada; usa una matriz vacía si no hay cmdlets que exportar.
CmdletsToExport = '*'

# Variables para exportar desde este módulo.
VariablesToExport = '*'

# Alias para exportar desde este módulo; para conseguir el mejor rendimiento, no uses caracteres comodines ni elimines la entrada; usa una matriz vacía si no hay alias que exportar.
AliasesToExport = '*'

# Recursos de DSC que se exportarán de este módulo
# DscResourcesToExport = @()

# Lista de todos los módulos empaquetados con este módulo
# ModuleList = @()

# Lista de todos los paquetes con este módulo.
# FileList = @()

# Datos privados que se pasan al módulo especificado en RootModule/ModuleToProcess. Pueden contener también una tabla hash PSData con metadatos del módulo adicionales usados por PowerShell.
PrivateData = @{

    PSData = @{

        # Etiquetas aplicadas a este módulo. Ayudan a encontrar el módulo en las galerías en línea.
        # Tags = @()

        # Dirección URL a la licencia de este módulo.
        # LicenseUri = ''

        # Una dirección URL al sitio web principal de este proyecto.
        # ProjectUri = ''

        # Una dirección URL a un icono que representa este módulo.
        # IconUri = ''

        # ReleaseNotes de este módulo
        # ReleaseNotes = ''

    } # Fin de la tabla hash PSData

} # Fin de la tabla hash PrivateData

# URI de HelpInfo de este módulo
# HelpInfoURI = ''

# Prefijo predeterminado para los comandos exportados desde este módulo. Invalide el prefijo predeterminado mediante Import-Module -Prefix.
# DefaultCommandPrefix = ''

}
