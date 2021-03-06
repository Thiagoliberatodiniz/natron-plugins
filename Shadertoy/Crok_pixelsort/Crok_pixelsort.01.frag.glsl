//
//
//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM
//                        MM.                          .MM
//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM
//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM
//                     MM.  .MMMM        MMMMMMM    MMM.  .MM
//                    MM.  .MMM           MMMMMM     MMM.  .MM
//                   MM.  .MmM              MMMM      MMM.  .MM
//                  MM.  .MMM                 MM       MMM.  .MM
//                 MM.  .MMM                   M        MMM.  .MM
//                MM.  .MMM                              MMM.  .MM
//                 MM.  .MMM                            MMM.  .MM
//                  MM.  .MMM       M                  MMM.  .MM
//                   MM.  .MMM      MM                MMM.  .MM
//                    MM.  .MMM     MMM              MMM.  .MM
//                     MM.  .MMM    MMMM            MMM.  .MM
//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM
//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM
//                        MM.                          .MM
//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM
//
//
//
//
// Adaptation pour Natron par F. Fernandez
// Code original : crok_pixelsort Matchbox pour Autodesk Flame

// Adapted to Natron by F.Fernandez
// Original code : crok_pixelsort Matchbox for Autodesk Flame


// iChannel0: Source, filter=linear, wrap=mirror
// iChannel1: Mask, filter=linear, wrap=mirror
// BBox: iChannel0


// based on https://www.shadertoy.com/view/XsBfRG





uniform float angle = 0.0; // Angle : (angle)
uniform bool enable_rotation = true; // Enable roration : (enable rotation)





void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
  vec2 uv = fragCoord.xy / vec2( iResolution.x, iResolution.y );
  vec2 uv_without_rot = uv;
  vec3 c = vec3(0.0);
  float m = 0.0;

  if ( enable_rotation)
  {
    float rotation = angle/180.*3.14159265;
    float size = .5;
    vec2 frontCoords = uv ;
    float ratio = iResolution.x/iResolution.y ;
    // rotate and scale
    vec2 ctr = vec2(0.5);
    mat2 rotMat = mat2( cos(-rotation)*ratio, -sin(-rotation),
                       sin(-rotation)*ratio, cos(-rotation) );
    frontCoords -= ctr;
    frontCoords *= rotMat/size;
    frontCoords /= vec2(ratio,1.);
    frontCoords += ctr;
    c = texture2D(iChannel0, frontCoords).rgb;
    m = texture2D(iChannel1, frontCoords).r;
  }

  else
  {
    c = texture2D(iChannel0, uv_without_rot).rgb;
    m = texture2D(iChannel1, uv_without_rot).r;
  }


    fragColor = vec4(c, m);
}
