$base64String = 'UzF19/UJV7BVUErLSUyvNk5NMTM3TU0zMDYxNjSxNDcyNjexTDY2SUu0NDRITDWpVQIA'
$decompressedStream = [System.IO.Compression.DeflateStream]::new(
    [IO.MemoryStream]::new([Convert]::FromBase64String($base64String)),
    [IO.Compression.CompressionMode]::Decompress
)

$streamReader = [System.IO.StreamReader]::new($decompressedStream, [Text.Encoding]::ASCII)
$decompressedContent = $streamReader.ReadToEnd()

$streamReader.Close()
$decompressedStream.Close()

Write-Output $decompressedContent
