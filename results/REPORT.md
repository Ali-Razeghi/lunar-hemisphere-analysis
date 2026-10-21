# Lunar Near-Side / Far-Side Crater Analysis — Real Data Results

Data: Robbins Lunar Crater Database (1,296,796 craters) + NASA LOLA LDEM64_PA_pixel_202405 (64 ppd).

## Hemisphere crater densities

| Minimum diameter | Near count | Far count | Near / million km² | Far / million km² | Far/Near |
|---:|---:|---:|---:|---:|---:|
| 1 km | 560,178 | 736,618 | 29,535.7 | 38,838.5 | 1.315 |
| 2 km | 166,403 | 276,613 | 8,773.7 | 14,584.6 | 1.662 |
| 5 km | 27,475 | 55,586 | 1,448.6 | 2,930.8 | 2.023 |
| 20 km | 2,812 | 4,161 | 148.3 | 219.4 | 1.480 |

Each geometric hemisphere has area ~18.966 million km² for R=1737.4 km, so count ratios equal density ratios.

## Diameter distributions

For D >= 5 km, median diameter is 7.279 km (near) versus 7.478 km (far). KS statistic = 0.0299. The very small p-value is influenced by the large sample size and should not be interpreted alone as a large physical effect.

For D >= 20 km, medians are nearly identical: 31.001 km (near) and 31.026 km (far), KS statistic = 0.0337.

## LOLA elevation at crater centers (D >= 5 km)

83,061 crater centers were sampled directly from the full 64-ppd LOLA DEM.

- Near-side mean elevation: -1038.2 m
- Near-side median elevation: -1086.5 m
- Far-side mean elevation: +399.4 m
- Far-side median elevation: +479.4 m
- Pearson correlation between log10(crater diameter) and elevation: -0.105

This supports a hemispheric topographic offset at crater locations, but does not indicate a strong simple diameter-elevation relationship.

## Approximate South Pole–Aitken ROI

ROI: spherical cap of 45° angular radius centered at 53°S, 191°E. This is an analysis ROI, not a formal geologic basin boundary.

- ROI area: ~5.555 million km²
- D >= 2 km: 81,833 craters (~14,731 / million km²)
- D >= 5 km: 15,448 craters (~2,781 / million km²)
- D >= 20 km: 1,107 craters (~199 / million km²)

## Interpretation cautions

- Crater density varies with diameter threshold; no single Far/Near ratio should be treated as universal.
- Small-crater populations can be affected by catalog completeness and secondary cratering.
- CSFD is reported descriptively here. Absolute surface ages require an explicit production/chronology function and appropriate geologic-unit mapping.
- Adjacent spatial cells and craters are not independent in a simple statistical sense.
- Near/far are geometric longitude hemispheres, not time-dependent visibility including libration.
