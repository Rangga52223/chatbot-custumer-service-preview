-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 18 Sep 2025 pada 09.33
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `electric_store`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `chat_log`
--

CREATE TABLE `chat_log` (
  `chat_id` char(36) NOT NULL,
  `user_id` char(36) NOT NULL,
  `chat_user` text NOT NULL,
  `chat_bot` text NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `chat_log`
--

INSERT INTO `chat_log` (`chat_id`, `user_id`, `chat_user`, `chat_bot`, `created_at`) VALUES
('117be75c-5294-4af7-b5ae-ec72ccd927b2', '21ccf5e0-9240-11f0-bbde-0068eb3251c5', 'Tadi saya ingin tahu apa?', 'Tentu, saya siap membantu Anda. Untuk menjawab pertanyaan Anda, saya perlu tahu lebih lanjut tentang kebutuhan dan pertanyaan Anda terkait toko online. Silakan beritahu saya apa yang ingin Anda ketahui atau butuhkan bantuan untuk toko online tersebut.', '2025-09-17 19:09:03'),
('12f6acf2-9ec1-4f88-9029-6bdca2e79cba', '21ccf5e0-9240-11f0-bbde-0068eb3251c5', 'Rekomendasi televisi yang murah dan bagus.', 'Berikut beberapa rekomendasi televisi yang murah dan bagus: Samsung Smart TV 55 Inch, LG OLED TV 65 Inch, Sony Bravia 50 Inch 4K, TCL Android TV 43 Inch, Panasonic LED TV 40 Inch, Sharp Aquos 32 HD dan Hisense 70 Inch ULED 4K. Semua produk ini memiliki harga Rp.3500000.00 dan garansi yang berbeda-beda.', '2025-09-17 19:50:02'),
('2957bc99-7770-438c-843b-dd05103dc9e5', '21ccf5e0-9240-11f0-bbde-0068eb3251c5', 'Tadi saya chat antara LG OLED TV 65 Inch dan Sony Bravia 50 Inch. Bagus mana ya? Saya lupa', 'Selamat datang kembali! Saya senang bisa membantu Anda hari ini lagi. Apakah ada sesuatu yang ingin Anda ketahui atau butuhkan bantuan terkait produk, garansi, transaksi, atau pengiriman di toko online kami?\n\n(Perlu diingat bahwa saya sudah menjawab pertanyaan yang sama sebelumnya dalam chat ini, jadi jika Anda telah membaca jawaban saya sebelumnya, silakan cek kembali chat sebelumnya untuk mendapatkan jawaban yang relevan.)', '2025-09-17 19:45:18'),
('51a15cb1-0747-4285-8313-c9d085aaca19', '21ccf5e0-9240-11f0-bbde-0068eb3251c5', 'Apa saja televisi yang tersedia', 'Tersedia beberapa model televisi dengan harga Rp.3500000.00, yaitu Samsung Smart TV 55 Inch, LG OLED TV 65 Inch, Sony Bravia 50 Inch 4K, TCL Android TV 43 Inch, Panasonic LED TV 40 Inch, Sharp Aquos 32 Inch HD, Hisense 70 Inch ULED 4K, Philips Ambilight 55 Inch, Xiaomi Mi TV 4S 43 Inch, dan Polytron Cinemax Soundbar 50 Inch.', '2025-09-17 21:00:51'),
('54a90ca6-3d8b-40f1-a4a2-f38e2f86d508', '21ccf5e0-9240-11f0-bbde-0068eb3251c5', 'tadi saya chat apa saja ya?', 'Senang sekali Anda kembali ke platform toko online kami! Berikut beberapa rekomendasi televisi yang murah dan bagus: Samsung Smart TV 55 Inch, LG OLED TV 65 Inch, Sony Bravia 50 Inch 4K, TCL Android TV 43 Inch, Panasonic LED TV 40 Inch, Sharp Aquos 32 HD dan Hisense 70 Inch ULED 4K. Semua produk ini memiliki harga Rp.3500000.00 dan garansi yang berbeda-beda.\n\nApakah Anda ingin tahu lebih lanjut tentang salah satu produk tersebut? Atau mungkin Anda memiliki pertanyaan lain terkait toko online kami?\n\n(Pastikan untuk menanyakan chat sebelumnya jika Anda sudah memiliki pertanyaan yang sama. Saya akan senang membantu Anda dengan jawaban yang relevan.)', '2025-09-17 19:57:04'),
('a8175e30-458f-4dcc-af6d-65fbfb5b7c17', '21ccf5e0-9240-11f0-bbde-0068eb3251c5', 'Saya mau cek transaksi saya dengan ID B78D9633-9240-11F0-BBDE-0068EB3251C5', 'Transaksi dengan ID B78D9633-9240-11F0-BBDE-0068EB3251C5 tidak ditemukan, silakan cek kembali transaksi Anda.', '2025-09-17 18:47:29'),
('cfee245f-155a-48d9-a915-5e86ed432f32', '21ccf5e0-9240-11f0-bbde-0068eb3251c5', 'tadi saya chat tentang apa?', 'Selamat datang di platform toko online kami! Apakah Anda memiliki pertanyaan atau memerlukan bantuan terkait produk, garansi, transaksi, atau pengiriman? Saya berada di sini untuk membantu Anda.\n\nPastikan untuk menanyakan chat sebelumnya jika Anda sudah memiliki pertanyaan yang sama. Saya akan senang membantu Anda dengan jawaban yang relevan.\n\nBagaimana saya dapat membantu Anda hari ini?', '2025-09-17 19:14:38'),
('e9a3274f-10cc-4208-a7e5-68c44bf515e7', '21ccf5e0-9240-11f0-bbde-0068eb3251c5', 'mesin cuci apa yang paling murah di bawah 3jt?', 'Saya senang sekali Anda menggunakan layanan kami! Berikut beberapa rekomendasi televisi yang murah dan bagus:\n\n1. Samsung Smart TV 55 Inch\n2. LG OLED TV 65 Inch\n3. Sony Bravia 50 Inch 4K\n4. TCL Android TV 43 Inch\n5. Panasonic LED TV 40 Inch\n6. Sharp Aquos 32 HD\n7. Hisense 70 Inch ULED 4K\n\nSemua produk ini memiliki harga Rp.3500000.00 dan garansi yang berbeda-beda.\n\nApakah Anda ingin tahu lebih lanjut tentang salah satu produk tersebut? Atau mungkin Anda memiliki pertanyaan lain terkait toko online kami?\n\n(Pastikan untuk menanyakan chat sebelumnya jika Anda sudah memiliki pertanyaan yang sama. Saya akan senang membantu Anda dengan jawaban yang relevan.)', '2025-09-17 21:25:16');

-- --------------------------------------------------------

--
-- Struktur dari tabel `produk`
--

CREATE TABLE `produk` (
  `product_id` char(36) NOT NULL,
  `product_name` varchar(150) NOT NULL,
  `description` text DEFAULT NULL,
  `harga` decimal(12,2) NOT NULL DEFAULT 0.00,
  `garansi` varchar(50) DEFAULT NULL,
  `product_type` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `produk`
--

INSERT INTO `produk` (`product_id`, `product_name`, `description`, `harga`, `garansi`, `product_type`, `created_at`) VALUES
('138b16e8-923e-11f0-bbde-0068eb3251c5', 'Samsung Washing Machine 8 Kg Front Load', 'Mesin cuci front load 8 Kg dengan fitur hemat energi.', 4500000.00, '6 Bulan', 2, '2025-09-15 14:12:56'),
('138b170f-923e-11f0-bbde-0068eb3251c5', 'LG TurboWash 9 Kg Front Load', 'Mesin cuci front load 9 Kg dengan teknologi TurboWash cepat dan bersih.', 4500000.00, '1 Tahun', 2, '2025-09-15 14:12:56'),
('138b1716-923e-11f0-bbde-0068eb3251c5', 'Panasonic Washing Machine 7 Kg Top Load', 'Mesin cuci top load 7 Kg dengan fitur pengering cepat.', 4500000.00, '6 Bulan', 2, '2025-09-15 14:12:56'),
('138b171a-923e-11f0-bbde-0068eb3251c5', 'Sharp Fully Automatic Washer 10 Kg', 'Mesin cuci otomatis 10 Kg dengan drum besar dan awet.', 4500000.00, '1 Tahun', 2, '2025-09-15 14:12:56'),
('138b171f-923e-11f0-bbde-0068eb3251c5', 'Toshiba Washing Machine 7.5 Kg', 'Mesin cuci 7.5 Kg dengan sistem hemat listrik dan air.', 4500000.00, '2 Tahun', 2, '2025-09-15 14:12:56'),
('138b1723-923e-11f0-bbde-0068eb3251c5', 'Polytron Zeromatic Belleza 8 Kg', 'Mesin cuci 8 Kg dengan desain elegan dan teknologi Zeromatic.', 4500000.00, '6 Bulan', 2, '2025-09-15 14:12:56'),
('138b1728-923e-11f0-bbde-0068eb3251c5', 'Electrolux UltimateCare 11 Kg', 'Mesin cuci 11 Kg dengan teknologi UltimateCare untuk pakaian lebih awet.', 4500000.00, '6 Bulan', 2, '2025-09-15 14:12:56'),
('138b172b-923e-11f0-bbde-0068eb3251c5', 'Hitachi Washing Machine 12 Kg', 'Mesin cuci 12 Kg dengan kapasitas besar dan performa tinggi.', 4500000.00, '2 Tahun', 2, '2025-09-15 14:12:56'),
('138b172f-923e-11f0-bbde-0068eb3251c5', 'Sanken Twin Tub Washing Machine 9 Kg', 'Mesin cuci twin tub 9 Kg, cocok untuk keluarga besar.', 4500000.00, '2 Tahun', 2, '2025-09-15 14:12:56'),
('138b1734-923e-11f0-bbde-0068eb3251c5', 'Aqua Japan Washing Machine 10 Kg', 'Mesin cuci 10 Kg dengan teknologi pendingin motor dan daya rendah.', 4500000.00, '6 Bulan', 2, '2025-09-15 14:12:56'),
('b8073dea-923e-11f0-bbde-0068eb3251c5', 'Samsung 2 Door Refrigerator 300L', 'Kulkas 2 pintu hemat energi dengan kapasitas besar dan fitur pendinginan merata.', 5000000.00, '6 Bulan', 3, '2025-09-15 14:17:32'),
('b8073e1c-923e-11f0-bbde-0068eb3251c5', 'LG InstaView Door-in-Door 450L', 'Kulkas premium dengan pintu transparan, teknologi inverter, dan hemat listrik.', 5000000.00, '6 Bulan', 3, '2025-09-15 14:17:32'),
('b8073e24-923e-11f0-bbde-0068eb3251c5', 'Panasonic Refrigerator 250L', 'Kulkas hemat energi dengan kompartemen fleksibel untuk menyimpan berbagai bahan makanan.', 5000000.00, '6 Bulan', 3, '2025-09-15 14:17:32'),
('b8073e2b-923e-11f0-bbde-0068eb3251c5', 'Sharp Side by Side Refrigerator 500L', 'Kulkas besar dengan sistem pendingin cepat dan rak yang luas.', 5000000.00, '2 Tahun', 3, '2025-09-15 14:17:32'),
('b8073e32-923e-11f0-bbde-0068eb3251c5', 'Toshiba Refrigerator 220L', 'Kulkas kompak yang cocok untuk keluarga kecil dengan konsumsi daya rendah.', 5000000.00, '6 Bulan', 3, '2025-09-15 14:17:32'),
('b8073e38-923e-11f0-bbde-0068eb3251c5', 'Polytron Belleza Inverter 320L', 'Kulkas 2 pintu dengan desain elegan, hemat energi, dan pendinginan cepat.', 5000000.00, '6 Bulan', 3, '2025-09-15 14:17:32'),
('b8073e3e-923e-11f0-bbde-0068eb3251c5', 'Hitachi French Door Refrigerator 600L', 'Kulkas modern dengan freezer besar, fitur smart cooling, dan kapasitas ekstra.', 5000000.00, '2 Tahun', 3, '2025-09-15 14:17:32'),
('b8073e45-923e-11f0-bbde-0068eb3251c5', 'Aqua Japan Refrigerator 280L', 'Kulkas efisien dengan pendinginan merata dan desain ramping.', 5000000.00, '1 Tahun', 3, '2025-09-15 14:17:32'),
('b8073e4b-923e-11f0-bbde-0068eb3251c5', 'Sanken Refrigerator 200L', 'Kulkas sederhana dengan daya rendah, harga terjangkau, dan desain praktis.', 5000000.00, '6 Bulan', 3, '2025-09-15 14:17:32'),
('b8073e52-923e-11f0-bbde-0068eb3251c5', 'Electrolux NutriFresh Inverter 400L', 'Kulkas dengan teknologi NutriFresh yang menjaga kesegaran makanan lebih lama.', 5000000.00, '6 Bulan', 3, '2025-09-15 14:17:32'),
('dd0cd3e2-923d-11f0-bbde-0068eb3251c5', 'Samsung Smart TV 55 Inch', 'Smart TV layar lebar dengan resolusi tinggi untuk hiburan keluarga.', 3500000.00, '2 Tahun', 1, '2025-09-15 14:11:24'),
('dd0cd410-923d-11f0-bbde-0068eb3251c5', 'LG OLED TV 65 Inch', 'TV OLED premium dengan kualitas gambar tajam dan warna akurat.', 3500000.00, '1 Tahun', 1, '2025-09-15 14:11:24'),
('dd0cd416-923d-11f0-bbde-0068eb3251c5', 'Sony Bravia 50 Inch 4K', 'TV 4K dengan teknologi Bravia Engine untuk detail lebih halus.', 3500000.00, '6 Bulan', 1, '2025-09-15 14:11:24'),
('dd0cd41a-923d-11f0-bbde-0068eb3251c5', 'TCL Android TV 43 Inch', 'Android TV dengan dukungan Google Assistant dan aplikasi streaming.', 3500000.00, '6 Bulan', 1, '2025-09-15 14:11:24'),
('dd0cd41f-923d-11f0-bbde-0068eb3251c5', 'Panasonic LED TV 40 Inch', 'TV LED hemat energi dengan tampilan natural dan ukuran 40 inch.', 3500000.00, '6 Bulan', 1, '2025-09-15 14:11:24'),
('dd0cd423-923d-11f0-bbde-0068eb3251c5', 'Sharp Aquos 32 Inch HD', 'TV HD ringkas dengan suara jernih, cocok untuk kamar tidur.', 3500000.00, '6 Bulan', 1, '2025-09-15 14:11:24'),
('dd0cd428-923d-11f0-bbde-0068eb3251c5', 'Hisense 70 Inch ULED 4K', 'TV ULED 70 inch dengan kualitas gambar luar biasa dan dukungan HDR.', 3500000.00, '6 Bulan', 1, '2025-09-15 14:11:24'),
('dd0cd42c-923d-11f0-bbde-0068eb3251c5', 'Philips Ambilight 55 Inch', 'Smart TV dengan fitur Ambilight yang menyinari dinding sesuai gambar.', 3500000.00, '6 Bulan', 1, '2025-09-15 14:11:24'),
('dd0cd431-923d-11f0-bbde-0068eb3251c5', 'Xiaomi Mi TV 4S 43 Inch', 'Smart TV dengan MIUI TV OS dan dukungan aplikasi streaming populer.', 3500000.00, '6 Bulan', 1, '2025-09-15 14:11:24'),
('dd0cd435-923d-11f0-bbde-0068eb3251c5', 'Polytron Cinemax Soundbar 50 Inch', 'Smart TV dengan soundbar terintegrasi untuk kualitas audio lebih baik.', 3500000.00, '6 Bulan', 1, '2025-09-15 14:11:24');

-- --------------------------------------------------------

--
-- Struktur dari tabel `stok`
--

CREATE TABLE `stok` (
  `id_stok` char(36) NOT NULL,
  `id_produk` char(36) NOT NULL,
  `kuantitas` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `stok`
--

INSERT INTO `stok` (`id_stok`, `id_produk`, `kuantitas`) VALUES
('19d3d8d8-923f-11f0-bbde-0068eb3251c5', 'dd0cd3e2-923d-11f0-bbde-0068eb3251c5', 8),
('19d3f22b-923f-11f0-bbde-0068eb3251c5', 'dd0cd410-923d-11f0-bbde-0068eb3251c5', 20),
('19d3f2e0-923f-11f0-bbde-0068eb3251c5', 'dd0cd416-923d-11f0-bbde-0068eb3251c5', 25),
('19d3f32f-923f-11f0-bbde-0068eb3251c5', 'dd0cd41a-923d-11f0-bbde-0068eb3251c5', 17),
('19d3f371-923f-11f0-bbde-0068eb3251c5', 'dd0cd41f-923d-11f0-bbde-0068eb3251c5', 8),
('19d3f3b5-923f-11f0-bbde-0068eb3251c5', 'dd0cd423-923d-11f0-bbde-0068eb3251c5', 37),
('19d3f41a-923f-11f0-bbde-0068eb3251c5', 'dd0cd428-923d-11f0-bbde-0068eb3251c5', 13),
('19d3f47e-923f-11f0-bbde-0068eb3251c5', 'dd0cd42c-923d-11f0-bbde-0068eb3251c5', 3),
('19d44605-923f-11f0-bbde-0068eb3251c5', 'dd0cd431-923d-11f0-bbde-0068eb3251c5', 24),
('19d44702-923f-11f0-bbde-0068eb3251c5', 'dd0cd435-923d-11f0-bbde-0068eb3251c5', 13),
('19d44771-923f-11f0-bbde-0068eb3251c5', '138b16e8-923e-11f0-bbde-0068eb3251c5', 43),
('19d447d6-923f-11f0-bbde-0068eb3251c5', '138b170f-923e-11f0-bbde-0068eb3251c5', 24),
('19d4482c-923f-11f0-bbde-0068eb3251c5', '138b1716-923e-11f0-bbde-0068eb3251c5', 43),
('19d4486c-923f-11f0-bbde-0068eb3251c5', '138b171a-923e-11f0-bbde-0068eb3251c5', 39),
('19d448c0-923f-11f0-bbde-0068eb3251c5', '138b171f-923e-11f0-bbde-0068eb3251c5', 18),
('19d4491e-923f-11f0-bbde-0068eb3251c5', '138b1723-923e-11f0-bbde-0068eb3251c5', 23),
('19d44982-923f-11f0-bbde-0068eb3251c5', '138b1728-923e-11f0-bbde-0068eb3251c5', 8),
('19d449d9-923f-11f0-bbde-0068eb3251c5', '138b172b-923e-11f0-bbde-0068eb3251c5', 20),
('19d44a1e-923f-11f0-bbde-0068eb3251c5', '138b172f-923e-11f0-bbde-0068eb3251c5', 28),
('19d44a58-923f-11f0-bbde-0068eb3251c5', '138b1734-923e-11f0-bbde-0068eb3251c5', 29),
('19d44a91-923f-11f0-bbde-0068eb3251c5', 'b8073dea-923e-11f0-bbde-0068eb3251c5', 9),
('19d44acb-923f-11f0-bbde-0068eb3251c5', 'b8073e1c-923e-11f0-bbde-0068eb3251c5', 8),
('19d44b03-923f-11f0-bbde-0068eb3251c5', 'b8073e24-923e-11f0-bbde-0068eb3251c5', 13),
('19d44b3a-923f-11f0-bbde-0068eb3251c5', 'b8073e2b-923e-11f0-bbde-0068eb3251c5', 40),
('19d44b72-923f-11f0-bbde-0068eb3251c5', 'b8073e32-923e-11f0-bbde-0068eb3251c5', 12),
('19d44bab-923f-11f0-bbde-0068eb3251c5', 'b8073e38-923e-11f0-bbde-0068eb3251c5', 38),
('19d44be1-923f-11f0-bbde-0068eb3251c5', 'b8073e3e-923e-11f0-bbde-0068eb3251c5', 2),
('19d44c17-923f-11f0-bbde-0068eb3251c5', 'b8073e45-923e-11f0-bbde-0068eb3251c5', 46),
('19d44c50-923f-11f0-bbde-0068eb3251c5', 'b8073e4b-923e-11f0-bbde-0068eb3251c5', 24),
('19d44c88-923f-11f0-bbde-0068eb3251c5', 'b8073e52-923e-11f0-bbde-0068eb3251c5', 31);

-- --------------------------------------------------------

--
-- Struktur dari tabel `transaction`
--

CREATE TABLE `transaction` (
  `transaction_id` char(36) NOT NULL,
  `user_id` char(36) NOT NULL,
  `id_produk` char(36) NOT NULL,
  `quantity` int(11) NOT NULL,
  `status` enum('pending','pengiriman','selesai') NOT NULL DEFAULT 'pending',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `total_harga` decimal(12,2) DEFAULT 0.00
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `transaction`
--

INSERT INTO `transaction` (`transaction_id`, `user_id`, `id_produk`, `quantity`, `status`, `created_at`, `total_harga`) VALUES
('b78d94d0-9240-11f0-bbde-0068eb3251c5', '21ccf5b9-9240-11f0-bbde-0068eb3251c5', 'dd0cd3e2-923d-11f0-bbde-0068eb3251c5', 2, 'selesai', '2025-08-15 03:30:00', 7000000.00),
('b78d955b-9240-11f0-bbde-0068eb3251c5', '21ccf5e0-9240-11f0-bbde-0068eb3251c5', '138b170f-923e-11f0-bbde-0068eb3251c5', 1, 'pending', '2025-08-20 07:15:00', 4500000.00),
('b78d9633-9240-11f0-bbde-0068eb3251c5', '21ccf5e6-9240-11f0-bbde-0068eb3251c5', 'b8073e2b-923e-11f0-bbde-0068eb3251c5', 3, 'pending', '2025-08-25 02:00:00', 15000000.00);

--
-- Trigger `transaction`
--
DELIMITER $$
CREATE TRIGGER `transaction_before_insert` BEFORE INSERT ON `transaction` FOR EACH ROW BEGIN
    DECLARE harga_produk DECIMAL(12,2);
    SELECT harga INTO harga_produk FROM produk WHERE product_id = NEW.id_produk;
    SET NEW.total_harga = NEW.quantity * harga_produk;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `transaction_before_update` BEFORE UPDATE ON `transaction` FOR EACH ROW BEGIN
    DECLARE harga_produk DECIMAL(12,2);
    SELECT harga INTO harga_produk FROM produk WHERE product_id = NEW.id_produk;
    SET NEW.total_harga = NEW.quantity * harga_produk;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Struktur dari tabel `type`
--

CREATE TABLE `type` (
  `type_id` int(11) NOT NULL,
  `type_name` varchar(100) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `type`
--

INSERT INTO `type` (`type_id`, `type_name`, `created_at`) VALUES
(1, 'Televisi', '2025-09-15 13:59:33'),
(2, 'Mesin Cuci', '2025-09-15 13:59:33'),
(3, 'Kulkas', '2025-09-15 13:59:33');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `user_id` char(36) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`user_id`, `username`, `password`, `created_at`) VALUES
('21ccf5b9-9240-11f0-bbde-0068eb3251c5', 'Admin', 'admin123', '2025-09-15 14:27:39'),
('21ccf5e0-9240-11f0-bbde-0068eb3251c5', 'James', 'james123', '2025-09-15 14:27:39'),
('21ccf5e6-9240-11f0-bbde-0068eb3251c5', 'Alex', 'alex123', '2025-09-15 14:27:39'),
('21ccf5eb-9240-11f0-bbde-0068eb3251c5', 'Joko', 'joko123', '2025-09-15 14:27:39'),
('21ccf5ef-9240-11f0-bbde-0068eb3251c5', 'Mulyono', 'mulyono123', '2025-09-15 14:27:39');

-- --------------------------------------------------------

--
-- Struktur dari tabel `waranty_detail`
--

CREATE TABLE `waranty_detail` (
  `waranty_id` int(11) NOT NULL,
  `waranty_detail` text NOT NULL,
  `type_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `waranty_detail`
--

INSERT INTO `waranty_detail` (`waranty_id`, `waranty_detail`, `type_id`) VALUES
(1, 'Garansi 6 bulan panel dan sparepart, tidak termasuk kerusakan akibat jatuh atau cairan.', 1),
(2, 'Garansi 2 tahun panel, 1 tahun sparepart. Tidak berlaku jika ada modifikasi atau penggunaan tidak wajar.', 1),
(3, 'Garansi 6 bulan motor penggerak dan sparepart, berlaku untuk pemakaian rumah tangga normal.', 2),
(4, 'Garansi 2 tahun motor penggerak, 1 tahun sparepart. Tidak mencakup kerusakan akibat korsleting eksternal.', 2),
(5, 'Garansi 6 bulan untuk sparepart dan kelistrikan. Tidak berlaku bila ada kerusakan fisik.', 3),
(6, 'Garansi 2 tahun kompresor, 1 tahun sparepart. Tidak mencakup kerusakan akibat listrik tidak stabil.', 3);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `chat_log`
--
ALTER TABLE `chat_log`
  ADD PRIMARY KEY (`chat_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indeks untuk tabel `produk`
--
ALTER TABLE `produk`
  ADD PRIMARY KEY (`product_id`),
  ADD KEY `product_type` (`product_type`);

--
-- Indeks untuk tabel `stok`
--
ALTER TABLE `stok`
  ADD PRIMARY KEY (`id_stok`),
  ADD KEY `id_produk` (`id_produk`);

--
-- Indeks untuk tabel `transaction`
--
ALTER TABLE `transaction`
  ADD PRIMARY KEY (`transaction_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `id_produk` (`id_produk`);

--
-- Indeks untuk tabel `type`
--
ALTER TABLE `type`
  ADD PRIMARY KEY (`type_id`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indeks untuk tabel `waranty_detail`
--
ALTER TABLE `waranty_detail`
  ADD PRIMARY KEY (`waranty_id`),
  ADD KEY `fk_waranty_type` (`type_id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `type`
--
ALTER TABLE `type`
  MODIFY `type_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `waranty_detail`
--
ALTER TABLE `waranty_detail`
  MODIFY `waranty_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `chat_log`
--
ALTER TABLE `chat_log`
  ADD CONSTRAINT `chat_log_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`);

--
-- Ketidakleluasaan untuk tabel `produk`
--
ALTER TABLE `produk`
  ADD CONSTRAINT `produk_ibfk_1` FOREIGN KEY (`product_type`) REFERENCES `type` (`type_id`);

--
-- Ketidakleluasaan untuk tabel `stok`
--
ALTER TABLE `stok`
  ADD CONSTRAINT `stok_ibfk_1` FOREIGN KEY (`id_produk`) REFERENCES `produk` (`product_id`);

--
-- Ketidakleluasaan untuk tabel `transaction`
--
ALTER TABLE `transaction`
  ADD CONSTRAINT `transaction_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  ADD CONSTRAINT `transaction_ibfk_2` FOREIGN KEY (`id_produk`) REFERENCES `produk` (`product_id`);

--
-- Ketidakleluasaan untuk tabel `waranty_detail`
--
ALTER TABLE `waranty_detail`
  ADD CONSTRAINT `fk_waranty_type` FOREIGN KEY (`type_id`) REFERENCES `type` (`type_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
