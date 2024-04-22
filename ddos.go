package main

import (
    "fmt"
    "net"
    "time"
    "sync"
)

func sendUDPPackets(ip string, port int, duration time.Duration, numThreads int) {
    var totalSizeBytes int64
    packetsSentPerThread := make([]int, numThreads)

    var wg sync.WaitGroup
    wg.Add(numThreads)

    for i := 0; i < numThreads; i++ {
        go func(threadID int) {
            defer wg.Done()
            conn, err := net.Dial("udp", fmt.Sprintf("%s:%d", ip, port))
            if err != nil {
                fmt.Printf("Error occurred in thread %d: %v\n", threadID, err)
                return
            }
            defer conn.Close()

            bytesToSend := make([]byte, 1200) // 1200 bytes packet size
            start := time.Now()
            for time.Since(start) < duration {
                _, err := conn.Write(bytesToSend)
                if err != nil {
                    fmt.Printf("Error occurred in thread %d: %v\n", threadID, err)
                    return
                }
                packetsSentPerThread[threadID]++
                totalSizeBytes += int64(len(bytesToSend))
                time.Sleep(10 * time.Millisecond) // Delay to control the rate of packet sending
            }
        }(i)
    }

    wg.Wait()

    totalPacketsSent := 0
    for _, packets := range packetsSentPerThread {
        totalPacketsSent += packets
    }
    totalSizeMB := float64(totalSizeBytes) / (1024 * 1024) // Convert total size to MB
    fmt.Printf("Sent %d UDP packets, Total size: %.2f MB\n", totalPacketsSent, totalSizeMB)
}

func main() {
    fmt.Println("Starting UDP packet sender...")

    var ip string
    var port int
    var duration time.Duration
    var numThreads int

    fmt.Print("Enter the IP address of the target: ")
    fmt.Scanln(&ip)
    fmt.Print("Enter the port number of the target: ")
    fmt.Scanln(&port)
    fmt.Print("Enter the duration to send UDP packets (in seconds): ")
    fmt.Scanln(&duration)
    fmt.Print("Enter the number of threads/concurrent tasks: ")
    fmt.Scanln(&numThreads)

    sendUDPPackets(ip, port, duration, numThreads)
    fmt.Println("UDP packet sending completed.")
}
